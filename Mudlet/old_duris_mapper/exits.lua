
duris.CARDINAL_EXITS_LONG = {"north", "south", "east", "west", "northeast", "northwest", "southeast", "southwest", "up", "down"}

-- NOTE: Ordering reflects mudlet defaults for converting exits to numeric values
duris.CARDINAL_EXITS_SHORT = {"n", "ne", "nw", "e", "w", "s", "se", "sw", "u", "d"}

duris.CARDINAL_EXITS_SHRINK = {north = "n", south = "s", east = "e", west = "w", northeast = "ne", northwest = "nw", southeast = "se", southwest = "sw", up = "u", down = "d"}

duris.CARDINAL_EXITS_EXPAND = {n = "north", s = "south", e = "east", w = "west", ne = "northeast", nw = "northwest", se = "southeast", sw = "southwest", u = "up", d = "down"}

function duris.map:getExitNum(dir)
  if not duris.map:isCardinalExit(dir) then
    duris.log:error("Can't get an exit number for a non-cardinal direction!")
    return
  end
  local exit = duris.map:getShortExit(dir)
  for k,v in pairs(duris.CARDINAL_EXITS_SHORT) do
    if exit == v then
      return k
    end
  end

  duris.log:error("Unable to find exit number for direction "..exit)
end

function duris.map:isCardinalExit(command)
  local isCardinal = false

  if table.contains(duris.CARDINAL_EXITS_LONG, command) or table.contains(duris.CARDINAL_EXITS_SHORT, command) then
    isCardinal = true
  end

  return isCardinal
end

function duris.map:getShortExit(command)
  if table.contains(duris.CARDINAL_EXITS_SHORT, command) then
    return command
  elseif table.contains(duris.CARDINAL_EXITS_LONG, command) then
    
    return duris.CARDINAL_EXITS_SHRINK[command]
  end
end

function duris.map:connectExits(room_data)
  local exits = room_data.info.exits
  local room_id = room_data.info.num
  
  for direction, room in pairs(exits) do
    local dir_num = duris.map:getExitNum(direction)
    if roomExists(room) then
      duris.log:debug("The room exists, connecting stubs")
      --setExit(room_id, room, direction)
      setExitStub(room_id, dir_num, true)
      connectExitStub(room_id, dir_num)
      local stubs = getExitStubs(room_id)
--      if stubs and table.contains(stubs, dir_num) then
--        duris.log:debug("Removing stub in dir "..dir_num)
--        setExitStub(room_id, dir_num, 0)
--      end
    else
      duris.log:debug("Unexplored exit, creating stub")
      duris.log:debug("Setting stub in direction "..dir_num)
      setExitStub(room_id, dir_num, true) 
    end
  end
  duris.log:debug("Leaving connectExits()") 
end

function duris.map:connectSpecialExits()
  if not duris.map:isCardinalExit(duris.command) 
    and duris.command ~= "l" 
    and duris.command ~= "look" 
    and duris.command ~= "recall" then
    duris.log:debug("Saw special exit command ("..duris.command.."), linking to prior room")

    local special_exits = getSpecialExits(gmcp.room.info.num)
    if not table.contains(special_exits, duris.command) then
      addSpecialExit(duris.map.prior_room, gmcp.room.info.num, duris.command)
    end
  end

end