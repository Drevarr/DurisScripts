spell_names = spell_names or {}  -- Paste your big table here if desired
local function getSpellName(id)
    return spell_names[id] or ("ID:"..id)
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
