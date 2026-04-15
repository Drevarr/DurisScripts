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