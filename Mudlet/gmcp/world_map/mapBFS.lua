unpack = table.unpack or unpack

local function parseMap(mapString)
  local grid = {}
  for line in mapString:gmatch("[^\n]+") do
    table.insert(grid, line)
  end
  return grid
end

local function findChar(grid, char)
  for y = 1, #grid do
    local x = grid[y]:find(char, 1, true)
    if x then
      return x, y
    end
  end
end

local function nextMoveTowardTarget(mapString)
  local grid = parseMap(mapString)
  local width = #grid[1]
  local height = #grid

  local sx, sy = findChar(grid, "@")
  local tx, ty = findChar(grid, "P")
  if not sx or not tx then return nil end

  local queue = { {sx, sy} }
  local visited = {}
  local cameFrom = {}

  local function key(x, y) return x .. "," .. y end
  visited[key(sx, sy)] = true

  local directions = {
    {0, -1, "north"},
    {0,  1, "south"},
    {-1, 0, "west"},
    {1,  0, "east"},
  }

  while #queue > 0 do
    local node = table.remove(queue, 1)
    local x, y = node[1], node[2]

    if x == tx and y == ty then
      break
    end

    for _, d in ipairs(directions) do
      local nx, ny = x + d[1], y + d[2]
      local k = key(nx, ny)

      if nx >= 1 and nx <= width and ny >= 1 and ny <= height then
        local tile = grid[ny]:sub(nx, nx)
        if tile ~= "M" and not visited[k] then
          visited[k] = true
          cameFrom[k] = {x, y}
          table.insert(queue, {nx, ny})
        end
      end
    end
  end

  -- reconstruct first step
  local cx, cy = tx, ty
  while cameFrom[key(cx, cy)] do
    local px, py = unpack(cameFrom[key(cx, cy)])
    if px == sx and py == sy then
      break
    end
    cx, cy = px, py
  end

  if cx == sx and cy == sy then return nil end

  if cx == sx and cy == sy - 1 then return "north" end
  if cx == sx and cy == sy + 1 then return "south" end
  if cx == sx - 1 and cy == sy then return "west" end
  if cx == sx + 1 and cy == sy then return "east" end
end

