-- Parse gmcp.room data from the mud

function duris.map:parseGmcpRoom()
--  local room_data = gmcp.room
  local zone_name = gmcp.room.info.zone

  -- Zone Handling
  if duris.map.current_zone ~= zone_name then
    duris.log:debug("Entered different zone")
    duris.map:setZone(zone_name)
  end
 
  -- Continent handling
  if gmcp.room.info.coord.cont == 1 then
    duris.log:debug("Continent room seen")
    local found_zone, zone_id = duris.map:isKnownZone(zone_name)
--    setGridMode(zone_id, true)
  end

  -- Room Handling
  duris.map.seen_room = gmcp.room.info.num
  duris.map.prior_room = duris.map.current_room

  if duris.map.seen_room == -1 then
    -- Eventually needs to work to map "nomap" areas...
    duris.log:debug("Can't find room based on mud id - none given")
  elseif roomExists(duris.map.seen_room) then
    if getRoomEnv(duris.map.seen_room) == 999 then
--      duris.log:debug("Existing room is a temp room - recreating")
--      deleteRoom(duris.map.seen_room)  -- Causes exits to get delinked!
--      duris.map:createRoom()
--      duris.map:connectExits(duris.map.prior_room_data) -- Relink missing exits
    else
      duris.log:debug("Found existing room - moving there")
      duris.map.current_room = duris.map.seen_room
      duris.map:connectSpecialExits()
      centerview(duris.map.seen_room)
    end
  else
    duris.log:debug("New room seen - creating...")
    --display(room_data)
    duris.map:createRoom()
  end
  duris.map.prior_room_data = table.copy(gmcp.room)
  duris.map.prior_zone_name = zone_name
end

function table.copy(t)
  local t2 = {}
  for k,v in pairs(t) do
    t2[k] = v
  end
  return t2
end