GMCP.vitals = GMCP.vitals or {
  curr = {},
  prev = {}
}

function gmcp_char_vitals()
  if not gmcp.Char or not gmcp.Char.Vitals then return end

  GMCP.store("vitals", {
    hp       = tonumber(gmcp.Char.Vitals.hp)      or 0,
    maxHp    = tonumber(gmcp.Char.Vitals.maxHp)   or 0,
    mana     = tonumber(gmcp.Char.Vitals.mana)    or 0,
    maxMana  = tonumber(gmcp.Char.Vitals.maxMana) or 0,
  })

  -- example comparison
  local prev = GMCP.vitals.prev
  local curr = GMCP.vitals.curr

  if prev.hp then
    local delta = curr.hp - prev.hp
    if delta ~= 0 then
      d("HP change: " .. delta)
    end
  end
end

