-- Handles all zone related functions


function duris.map:resetZone(zone_name)
  local zone_found, zone_id = duris.map:isKnownZone(zone_name)

  if not zone_found then
    duris.log:error("Zone not found - can't reset")
  else
    local rooms = getAreaRooms(zone_id)

    if not rooms then
      duris.log:info("No rooms to remove in "..zone_name)
      return
    end

    for room_name, room_id in pairs(rooms) do
      deleteRoom(room_id)
    end
    duris.log:info("Removed all rooms from zone "..zone_name)
  end
end

function duris.map:isKnownZone(zone_name)
  local zones = getAreaTable()
  local zone_found = false
  local found_zone_id = nil
  
  for known_zone_name, zone_id in pairs(zones) do
    if known_zone_name == zone_name then
      zone_found = true
      found_zone_id = zone_id
      duris.log:debug("Found zone as id "..zone_id)
      break
    end
  end

  
  return zone_found, found_zone_id

end

function duris.map:createZone(new_zone_name)
  local new_zone_id = nil

  if not duris.map:isKnownZone() then
    new_zone_id = addAreaName(new_zone_name)
    duris.log:debug("New zone "..new_zone_name.." created with id: "..new_zone_id)
  else
    duris.log:debug("Zone already exists, not creating new zone")
  end

  return new_zone_id
end

function duris.map:getZoneId(zone_name)
  local found, zone_id = duris.map:isKnownZone(zone_name)
  if not found then
    zone_id = duris.map:createZone(zone_name)
  end

  return zone_id
end

function duris.map:setZone(zone_name)
  
  -- Set this zone as the active zone
  local zone_id = duris.map:getZoneId(zone_name)
  if zone_id then
    duris.map.current_zone = zone_name
  else
    duris.map:error("Failed to set zone!")
  end
  duris.log:debug("Current zone is now: "..duris.map.current_zone)

end