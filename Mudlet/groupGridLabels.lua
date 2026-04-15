local TextGauge = require("scripts.textgauge")


function make_group_grid_labels()
GUIFlex.GroupGrid = Geyser.HBox:new({
  name = "GUIFlex.GroupGrid",
  x = 0, y = 0,
  width = "100%",
  height = "35%",
},GUIFlex.Box2)

for i=1,4 do
  GUIFlex["GroupButton"..i] = Geyser.Label:new({
    name = "GUIFlex.GroupButton"..i,
    clickCommand = "GroupButton "..i.." pressed",
    style = GUIFlex.GridButtonCSS,
  },GUIFlex.GroupGrid)
end
end
hp_vitals = TextGauge:new({
  width = 10,
  fillCharacter = "=",
  fillColor = "green",
  emptyCharacter = "=",
  overflowCharacter = "=",
  emptyColor = "dark_green",
  percentColor = "ghost_white",
  percentSymbolColor = "ghost_white",
  overflowColor = "medium_blue",
})

mv_vitals = TextGauge:new({
  width = 10,
  fillCharacter = "+",
  fillColor = "ansi_light_yellow",
  emptyCharacter = "+",
  overflowCharacter = "+",
  emptyColor = "ansi_yellow",
  percentColor = "ghost_white",
  percentSymbolColor = "ghost_white",
  overflowColor = "medium_blue",
})

GUIFlex.GroupButton1:cecho("<cyan>Drevarr\n<reset>HP:"..hp_vitals:setValue(80).."\nMV:"..mv_vitals:setValue(75))