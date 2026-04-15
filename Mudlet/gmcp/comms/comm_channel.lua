function gmcp_comm_channel()
    if not gmcp.Comm.Channel then return end
    local c = gmcp.Comm.Channel
    local colors = { nchat = "light_blue", tell = "cyan", say = "white" }  -- add more
    cecho(string.format("\n<%s>%s: %s\n", colors[c.channel] or "gray", c.sender, c.text))
    -- return true to suppress default output if desired
end
registerAnonymousEventHandler("gmcp.Comm.Channel", "gmcp_comm_channel")