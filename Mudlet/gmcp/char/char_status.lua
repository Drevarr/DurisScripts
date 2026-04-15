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