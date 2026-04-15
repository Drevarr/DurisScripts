--Char.AffectsGMCP.room = GMCP.room or {}

function gmcp_char_affects()
  if not gmcp.Char or not gmcp.Char.Affects then return end

  local affects = {}

  for _, aff in ipairs(gmcp.Char.Affects) do
    affects[aff.id] = {
      id       = aff.id,
      name     = aff.name,
      icon     = aff.icon,
      duration = tonumber(aff.duration) or 0,
    }
  end

  GMCP.store("affects", affects)

  -- OPTIONAL examples -------------------------------

  local prev = GMCP.affects.prev
  local curr = GMCP.affects.curr

  for id, aff in pairs(curr) do
    if aff.duration == 10 then
      cecho("\n<red>WARNING:</red> " .. aff.name .. " fading!")
    end
  end
  

  -- detect gained affects
  for id, aff in pairs(curr) do
    if not prev[id] then
      cecho("Gained affect: " .. aff.name)
    end
  end

  -- detect lost affects
  for id, aff in pairs(prev) do
    if not curr[id] then
      cecho("Lost affect: " .. aff.name)
    end
  end
end
