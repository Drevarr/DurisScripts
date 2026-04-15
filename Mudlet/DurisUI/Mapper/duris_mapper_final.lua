-- Duris GMCP Mapper Relative-Coordinate Based
-- Version 0.1.0
-- Author: Drevarr
-- License: Public Domain

mudlet = mudlet or {}
mudlet.mapper_script = true

map = map or {}
map.room_info = map.room_info or {}
map.last_room_vnum = map.last_room_vnum or nil


-- Terrain to Environment ID
local TERRAIN = {
  ["inside"]=263, ["city"]=263, ["field"]=258, ["forest"]=266,
  ["hills"]=267, ["mountains"]=259, ["desert"]=259,
  ["water swim"]=262, ["water noswim"]=260, ["ocean"]=268,
  ["underwater"]=268, ["underwater ground"]=268,
  ["no ground"]=271, ["tundra"]=271, ["snowy forest"]=272,
  ["swamp"]=261, ["lava"]=257,
  ["ud wild"]=261, ["ud city"]=263, ["ud inside"]=261,
  ["ud water swim"]=262, ["ud water noswim"]=260,
  ["ud no ground"]=263, ["ud mountains"]=264,
  ["ud slime"]=257, ["ud low ceilings"]=269,
  ["ud liquid mithril"]=261, ["ud mushroom forest"]=269,
  ["plane of fire"]=265, ["plane of air"]=263,
  ["plane of water"]=268, ["plane of earth"]=263,
  ["plane of ethereal"]=263, ["plane of astral"]=268,
  ["plane of avernus"]=260, ["negative plane"]=260,
  ["outer castle wall"]=263, ["castle gate"]=263, ["castle"]=257,
  ["patrolled road"]=260,
}

-- Direction Normalization
local EXITMAP = {
  n = "north", s = "south", e = "east", w = "west",
  ne = "northeast", nw = "northwest",
  se = "southeast", sw = "southwest",
  u = "up", d = "down",
}


-- Movement Vectors
local TELEPORT_OFFSET = { 1, 1, 1 }  -- large jump to avoid overlap

local MOVE = {
  north = { 0,  1,  0 }, south = { 0, -1,  0 },
  east  = { 1,  0,  0 }, west  = {-1,  0,  0 },
  northeast = { 1,  1,  0 }, northwest = {-1,  1,  0 },
  southeast = { 1, -1,  0 }, southwest = {-1, -1,  0 },
  up = { 0,  0,  1 }, down = { 0,  0, -1 },
}


-- Coordinate Calculation
local function calculateCoords(curr_vnum, prev_vnum, prev_exits)
  local ORIGIN = {0, 0, 0}

  if not prev_vnum then
    return { unpack(ORIGIN) }
  end

  local px, py, pz = getRoomCoordinates(prev_vnum)
  if not px or not py or not pz then
    return { unpack(ORIGIN) }
  end

  local coords = { px, py, pz }

  -- normal directional movement first
  for dir, dest in pairs(prev_exits or {}) do
    if dest == curr_vnum then
      local vector = MOVE[dir]
      if vector then
        for i = 1, 3 do
          coords[i] = coords[i] + vector[i]
        end
        return coords
      end
    end
  end

  -- TELEPORT DETECTED
  -- No exit from prev to curr, but we arrived
  for i = 1, 3 do
    coords[i] = coords[i] + TELEPORT_OFFSET[i]
  end

  return coords
end


-- Area / Zone Helpers
local function ensureArea(name)
  local areas = getAreaTable()
  if areas[name] then
    return areas[name]
  end

  local id = addAreaName(name)
  if id then
    cecho("<green>Created area: "..name.." ("..id..")\n")
  end
  return id
end


-- Room Creation
local function makeRoom(info)
  if getRoomName(info.vnum) then return end

  ensureArea(info.area)

  addRoom(info.vnum)
  setRoomName(info.vnum, info.name)
  setRoomArea(info.vnum, info.area)
  setRoomCoordinates(info.vnum, info.coords[1], info.coords[2], info.coords[3])

  if TERRAIN[info.environment] then
    setRoomEnv(info.vnum, TERRAIN[info.environment])
  end
end


-- Exit Linking
local function linkExits(info)
  for dir, dest in pairs(info.exits) do
    if getRoomName(dest) then
      setExit(info.vnum, dest, dir)
    else
      setExitStub(info.vnum, dir, true)
    end
  end
end


-- GMCP Handler
function map.onGMCP()
  local g = gmcp.Room.Info
  if not g or not g.num then return end

  local vnum = tonumber(g.num)

  -- Build exits first for coord calc
  local exits = {}
  for dir, dest in pairs(g.exits or {}) do
    exits[EXITMAP[dir] or dir] = tonumber(dest)
  end

  -- Calculate relative coordinates
  local coords = calculateCoords(
    vnum,
    map.last_room_vnum,
    map.room_info and map.room_info.exits
  )

  local info = {
    vnum = vnum,
    name = g.name or "Unknown",
    area = g.area or "Unknown",
    environment = g.environment,
    terrain = g.terrain,
    coords = coords,
    exits = exits,
  }

  map.room_info = info

  makeRoom(info)
  linkExits(info)
  -- Create a teleport exit back if one exists
  if map.last_room_vnum then
    for dir, dest in pairs(info.exits) do
      if dest == map.last_room_vnum then
        setExit(info.vnum, map.last_room_vnum, "out")
        break
      end
    end
  end
  centerview(info.vnum)

  map.last_room_vnum = info.vnum
end


registerAnonymousEventHandler("gmcp.Room.Info", "map.onGMCP")
