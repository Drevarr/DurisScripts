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