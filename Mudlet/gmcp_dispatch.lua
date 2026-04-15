GMCP = GMCP or {}

GMCP.last = {}
  Char.Affects
registerAnonymousEventHandler("gmcp", "GMCP.dispatch")

function GMCP.dispatch()
  if type(gmcp) ~= "table" then return end

  for ns, payload in pairs(gmcp) do
    if type(payload) == "table" then
      raiseEvent("gmcp" .. ns, payload)
      GMCP.deepDiff(ns, payload)
    end
  end
end

local function shallowCopy(t)
  local c = {}
  for k, v in pairs(t) do c[k] = v end
  return c
end

local function isArray(t)
  if type(t) ~= "table" then return false end
  local n = 0
  for k in pairs(t) do
    if type(k) ~= "number" then return false end
    n = n + 1
  end
  return n > 0
end

function GMCP.identity(ns, sub, item)
  if ns == "Char" and sub == "Affects" then
    return item.id
  elseif ns == "Group" and sub == "Status" then
    return item.name
  elseif ns == "Room" and (sub == "npcs" or sub == "items") then
    return item.vnum .. ":" .. (item.keyword or item.name or "")
  end
end

function GMCP.diffArray(ns, sub, newArr, oldArr)
  oldArr = oldArr or {}
  local oldIndex = {}
  local newIndex = {}

  for _, item in ipairs(oldArr) do
    local id = GMCP.identity(ns, sub, item)
    if id then oldIndex[id] = item end
  end

  for _, item in ipairs(newArr) do
    local id = GMCP.identity(ns, sub, item)
    if id then newIndex[id] = item end
  end

  -- added / updated
  for id, item in pairs(newIndex) do
    if not oldIndex[id] then
      raiseEvent("gmcp" .. ns .. sub .. "Added", item)
    elseif not table.equals(item, oldIndex[id]) then
      raiseEvent("gmcp" .. ns .. sub .. "Updated", item, oldIndex[id])
    end
  end

  -- removed
  for id, item in pairs(oldIndex) do
    if not newIndex[id] then
      raiseEvent("gmcp" .. ns .. sub .. "Removed", item)
    end
  end
end

function GMCP.deepDiff(ns, payload)
  GMCP.last[ns] = GMCP.last[ns] or {}

  for key, value in pairs(payload) do
    local old = GMCP.last[ns][key]

    if type(value) == "table" then
      if isArray(value) then
        GMCP.diffArray(ns, key, value, old)
      else
        raiseEvent("gmcp" .. ns .. key, value, old)
      end
    elseif value ~= old then
      raiseEvent("gmcp" .. ns .. key, value, old)
    end

    GMCP.last[ns][key] = shallowCopy(value)
  end
end

GMCP.Room = {}

function GMCP.Room:getInfo()
  return gmcp.Room and gmcp.Room.Info
end

function GMCP.Room:getID()
  local r = self:getInfo()
  return r and r.num
end

function GMCP.Room:getExits()
  local r = self:getInfo()
  return r and r.exits or {}
end

function GMCP.Room:getNPCs()
  local r = self:getInfo()
  return r and r.npcs or {}
end

function GMCP.Room:hasNPC(keyword)
  for _, n in ipairs(self:getNPCs()) do
    if n.keyword == keyword then return true end
  end
  return false
end

GMCP.Char = {}

function GMCP.Char:getVitals()
  return gmcp.Char and gmcp.Char.Vitals
end

function GMCP.Char:getHP()
  local v = self:getVitals()
  return v and v.hp, v and v.maxHp
end

function GMCP.Char:getMana()
  local v = self:getVitals()
  return v and v.mana, v and v.maxMana
end

function GMCP.Char:isFighting()
  local v = self:getVitals()
  return v and v.fighting ~= ""
end

function GMCP.Char:getAffects()
  return gmcp.Char and gmcp.Char.Affects or {}
end

function GMCP.Char:hasAffect(name)
  for _, a in ipairs(self:getAffects()) do
    if a.name == name then return true end
  end
  return false
end


