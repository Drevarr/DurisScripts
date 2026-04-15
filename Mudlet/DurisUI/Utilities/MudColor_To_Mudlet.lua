--[[
Convert MudColor test to Mudlet
Author: Drevarr
License: Public Domain

]]


local rgb = {
  L = {64, 64, 64},    l = {128, 128, 128},
  R = {255, 0, 0},     r = {128, 0, 0},
  G = {0, 255, 0},     g = {0, 128, 0},
  Y = {255, 255, 0},   y = {128, 128, 0},
  B = {0, 0, 255},     b = {0, 0, 128},
  M = {255, 0, 255},   m = {128, 0, 128},
  C = {0, 255, 255},   c = {0, 128, 128},
  W = {255, 255, 255}, w = {192, 192, 192},
}

local function hex(c)
  return string.format("%02X%02X%02X", c[1], c[2], c[3])
end


local renderers = {}

-- plain echo (strip everything)
renderers.echo = {
  reset = "",
  fg = function(_) return "" end,
  bg = function(_) return "" end,
  both = function(_, _) return "" end
}

-- decho (RGB)
renderers.decho = {
  reset = "<r>",
  fg = function(fg)
    return string.format("<%d,%d,%d>", fg[1], fg[2], fg[3])
  end,
  bg = function(bg)
    return string.format("<:%d,%d,%d>", bg[1], bg[2], bg[3])
  end,
  both = function(fg, bg)
    return string.format("<%d,%d,%d:%d,%d,%d>",
      fg[1], fg[2], fg[3],
      bg[1], bg[2], bg[3])
  end
}

-- hecho (hex)
renderers.hecho = {
  reset = "#r",
  fg = function(fg)
    return "#" .. hex(fg)
  end,
  bg = function(bg)
    return "" -- hecho has no true background
  end,
  both = function(fg, _)
    return "#" .. hex(fg)
  end
}

-- cecho (named colors — best-effort mapping)
local cechoNames = {
  R="red", r="ansiRed",
  G="green", g="ansiGreen",
  B="blue", b="ansiBlue",
  Y="yellow", y="ansiYellow",
  M="magenta", m="ansiMagenta",
  C="cyan", c="ansiCyan",
  W="white", w="ansiWhite",
  L="DimGrey", l="LightSlateGrey",
}

renderers.cecho = {
  reset = "<r>",
  fg = function(_, key)
    return "<" .. (cechoNames[key] or "white") .. ">"
  end,
  bg = function(_) return "" end,
  both = function(_, _, key)
    return "<" .. (cechoNames[key] or "white") .. ">"
  end
}


function convertMap(text, mode)
  local R = renderers[mode] or renderers.echo

  -- reset
  text = text:gsub("&[nN]", R.reset)

  -- &=BGFG
  text = text:gsub("&=([A-Za-z])([A-Za-z])", function(bg, fg)
    if not rgb[fg] then return "" end
    return R.both(rgb[fg], rgb[bg], fg)
  end)

  -- &+F
  text = text:gsub("&%+([A-Za-z])", function(c)
    if not rgb[c] then return "" end
    return R.fg(rgb[c], c)
  end)

  -- &-B
  text = text:gsub("&%-([A-Za-z])", function(c)
    if not rgb[c] then return "" end
    return R.bg(rgb[c], c)
  end)

  return text
end


