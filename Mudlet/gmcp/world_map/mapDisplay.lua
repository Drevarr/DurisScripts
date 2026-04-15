local rgb = {
  L = {0, 0, 0},       l = {64, 64, 64},
  R = {255, 0, 0},     r = {128, 0, 0},
  G = {0, 255, 0},     g = {0, 128, 0},
  Y = {255, 255, 0},   y = {128, 128, 0},
  B = {0, 0, 255},     b = {0, 0, 128},
  M = {255, 0, 255},   m = {128, 0, 128},
  C = {0, 255, 255},   c = {0, 128, 128},
  W = {255, 255, 255}, w = {192, 192, 192},
}

local function rgbTag(fg, bg)
  if fg and bg then
    return string.format("<%d,%d,%d:%d,%d,%d>",
      fg[1], fg[2], fg[3],
      bg[1], bg[2], bg[3])
  elseif fg then
    return string.format("<%d,%d,%d>", fg[1], fg[2], fg[3])
  elseif bg then
    return string.format("<:%d,%d,%d>", bg[1], bg[2], bg[3])
  end
end

function convertMapToRGB(text)
  -- reset (Mudlet default colors)
  text = text:gsub("&n", "<r>")

  -- both background + foreground
  text = text:gsub("&=([A-Za-z])([A-Za-z])", function(bg, fg)
    return rgbTag(rgb[fg], rgb[bg])
  end)

  -- foreground only
  text = text:gsub("&%+([A-Za-z])", function(c)
    return rgbTag(rgb[c], nil)
  end)

  -- background only
  text = text:gsub("&%-([A-Za-z])", function(c)
    return rgbTag(nil, rgb[c])
  end)

  return text
end


function showRoomMap(win)
  if not gmcp.Room.Map or not gmcp.Room.Map.map then return end
  clearWindow(win)
  decho(win, "\n"..convertMapToRGB(gmcp.Room.Map.map))
end