GMCP.room = GMCP.room or {}

local watchedNPCs = {
  ["the robin"] = true,
  ["a white rabbit"]   = true,
}



local function countNpcsByVnum(npcs)
  local t = {}

  for _, npc in ipairs(npcs or {}) do
    local vnum = npc.vnum
    if not t[vnum] then
      t[vnum] = {
        count = 0,
        name  = npc.name,        -- store one name
        keyword = npc.keyword,   -- optional, but useful
      }
    end
    t[vnum].count = t[vnum].count + 1
  end

  return t
end

function gmcp_room_info()
  if not gmcp.Room or not gmcp.Room.Info then return end
  local info = gmcp.Room.Info

  GMCP.store("room", {
    id      = info.num,
    name    = info.name,
    items   = info.items or {},
    npcs    = info.npcs or {},
    players = info.players or {},
    exits   = info.exits or {},
  })

  local prev = GMCP.room.prev
  local curr = GMCP.room.curr
  
  if prev.id == curr.id then
    local pNpcs = countNpcsByVnum(prev.npcs)
    local cNpcs = countNpcsByVnum(curr.npcs)
  
    for vnum, data in pairs(cNpcs) do
      local prevCount = pNpcs[vnum] and pNpcs[vnum].count or 0
  
      if data.count > prevCount then
        if watchedNPCs[data.name] then
          echo("Spawned: " .. data.name)
          send("kill "..data.keyword)
        end
      end
    end
  
    for vnum, data in pairs(pNpcs) do
      local currCount = cNpcs[vnum] and cNpcs[vnum].count or 0
  
      if data.count > currCount then
        if watchedNPCs[data.name] then
          echo("Despawned: " .. data.name)
        end
      end
    end
  end
end


