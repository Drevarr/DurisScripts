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