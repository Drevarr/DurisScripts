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