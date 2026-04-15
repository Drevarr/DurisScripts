-- Persistent storage tables
local currentAffects = currentAffects or {}
local vitals = vitals or {}
local targetInfo = targetInfo or {}
local groupMembers = groupMembers or {}
local questInfo = questInfo or {}
local roomInfo = roomInfo or {}


spell_names = spell_names or {}  -- Paste your big table here if desired
local function getSpellName(id)
    return spell_names[id] or ("ID:"..id)
end

function gmcpVarByPath(varPath)
  local temp = gmcp
  for varStep in varPath:gmatch("([^\\.]+)") do
    if temp and temp[varStep] then
      temp = temp[varStep]
    else
      return nil
    end
  end
  return temp
end


-- Wires up GMCP subscriptions for a gauge.
-- statName is the short version of the stat name to show after the value (mv, hp, etc)
local function wireGaugeUpdate(gauge, valueVarName, maxVarName, statName, eventName)
  local function doUpdate()
    local current = gmcpVarByPath(valueVarName) or 0
    local max = gmcpVarByPath(maxVarName) or 0
    if max > 0 then
      gauge:setValue(current, max, current.."/"..max.." "..statName)
    else
      gauge:setValue(0, 1, "")
    end
  end
  registerEventHandler(eventName, doUpdate)
end



function gmcp_char_affects()
    if not gmcp.Char.Affects then return end

    local newLookup = {}
    for _, aff in ipairs(gmcp.Char.Affects) do
        newLookup[aff.id] = { name = aff.name, duration = aff.duration, icon = aff.icon }
    end

    -- Added/Updated
    for id, data in pairs(newLookup) do
        local old = currentAffects[id]
        if not old then
            -- change cecho to update table in buff window
            cecho(string.format("\n<green>[BUFF+] %s <gray>(%s)<white> - %d sec\n", data.name, getSpellName(id), comma_value(data.duration)))
        elseif old.duration ~= data.duration then

            cecho(string.format("\n<yellow>[TICK] %s <gray>(%s)<white>: %d → %d sec\n", data.name, getSpellName(id), comma_value(old.duration), comma_value(data.duration)))
        end
        currentAffects[id] = data
    end

    -- Removed
    for id, old in pairs(currentAffects) do
        if not newLookup[id] then
            -- change cecho to update table in buff window
            cecho(string.format("\n<red>[BUFF-] %s <gray>(%s)<white> expired\n", old.name, getSpellName(id)))
            currentAffects[id] = nil
        end
    end
end
registerAnonymousEventHandler("gmcp.Char.Affects", "gmcp_char_affects")

local oldTNL = nil
function gmcp_char_vitals()
    if not gmcp.Char.Vitals then return end
    vitals = gmcp.Char.Vitals

    -- Convert strings to numbers
    vitals.hp = tonumber(vitals.hp) or 0
    vitals.maxHp = tonumber(vitals.maxHp) or 0
    -- etc. for others if needed

    -- XP gain tracking
    local currentTNL = tonumber(vitals.tnl) or 0
    if oldTNL then
        if currentTNL < oldTNL then
            local gained = oldTNL - currentTNL
            local mobsNeeded = gained > 0 and math.ceil(currentTNL / gained) or "?"
            -- This is incorrect/ really just xp per round
            -- add a currentTNL < oldTNL check on kill experience elsewhere
            cecho(string.format("\n<cyan>[XP+] +%d XP | TNL: %d → %d | ~%s kills to level\n", gained, oldTNL, currentTNL, mobsNeeded))
        elseif currentTNL > oldTNL then
            cecho(string.format("\n<red>[XP-] TNL increased: %d → %d\n", oldTNL, currentTNL))
        end
    else
        cecho(string.format("\n<white>[INIT] TNL: %d\n", currentTNL))
    end
    oldTNL = currentTNL

    -- Update gauges here
    -- updateHPGauge(vitals.hp, vitals.maxHp)
end
registerAnonymousEventHandler("gmcp.Char.Vitals", "gmcp_char_vitals")


function gmcp_char_status()
    if not gmcp.Char.Status then return end
    local status = gmcp.Char.Status
    -- Detect level up
    if status.level and (not playerLevel or tonumber(status.level) > playerLevel) then
        playerLevel = tonumber(status.level)
        cecho(string.format("\n<yellow>*** LEVEL UP TO %d! ***\n", playerLevel))
    end
end
registerAnonymousEventHandler("gmcp.Char.Status", "gmcp_char_status")


function gmcp_combat_update()
    if not gmcp.Combat or not gmcp.Combat.Update or not gmcp.Combat.Update.target then return end
    targetInfo = gmcp.Combat.Update.target
    --Breaks on rescue, targetInfo gets set to <userData>
    local t = targetInfo
    cecho(string.format("\n<red>[TARGET] %s - %s (%d%%)\n", t.name or "?", t.health or "?", t.healthPercent or 0))
    -- auto-assist and update target gauges
end
registerAnonymousEventHandler("gmcp.Combat.Update", "gmcp_combat_update")


function gmcp_comm_channel()
    if not gmcp.Comm.Channel then return end
    local c = gmcp.Comm.Channel
    local colors = { nchat = "light_blue", tell = "cyan", say = "white" }  -- add more
    cecho(string.format("\n<%s>%s: %s\n", colors[c.channel] or "gray", c.sender, c.text))
    -- return true to suppress default output if desired
end
registerAnonymousEventHandler("gmcp.Comm.Channel", "gmcp_comm_channel")


function gmcp_group_status()
    if not gmcp.Group.Status then return end
    groupMembers = gmcp.Group.Status.members or {}
    -- Example: simple group list echo
    cecho("\n<green>--- Group (%d/%d) ---\n", #groupMembers, gmcp.Group.Status.maxSize or 0)
    for _, mem in ipairs(groupMembers) do
        local hpPct = mem.maxHp and mem.hp and math.floor(mem.hp / mem.maxHp * 100) or "?"
        local class = (type(mem.class) == "string") and mem.class or "PET"
        cecho(string.format("  %s [%s] %d%% HP\n", mem.name, mem.class or "?", hpPct))
    end
    -- Update group gauges and group window
end
registerAnonymousEventHandler("gmcp.Group.Status", "gmcp_group_status")


function gmcp_quest_status()
    if not gmcp.Quest.Status then return end
    questInfo = gmcp.Quest.Status
    if questInfo.active then
        cecho(string.format("\n<magenta>[QUEST] %d remaining: %s\n", questInfo.remaining or 0, questInfo.target or "?"))
    else
        cecho("\n<magenta>[QUEST] No active quest\n")
    end
end
registerAnonymousEventHandler("gmcp.Quest.Status", "gmcp_quest_status")


local currentZone = nil
function gmcp_room_info()
    if not gmcp.Room.Info then return end
    roomInfo = gmcp.Room.Info

    -- Zone/area change
    if roomInfo.area and roomInfo.area ~= currentZone then
        currentZone = roomInfo.area
        cecho(string.format("\n<orange>[ZONE] Entered %s\n", currentZone))
    end

    -- Room name display, use decho and convertMapToRGB()
    cecho(string.format("\n<white>%s\n", decho(convertMapToRGB(roomInfo.colored_name)) or roomInfo.name or "Unknown Room"))
end
registerAnonymousEventHandler("gmcp.Room.Info", "gmcp_room_info")