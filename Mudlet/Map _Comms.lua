MapUI = MapUI or {}

-- Tab styling
MapUI.styles = {
  tabInactive = [[
    background-color: #222222;
    color: #AAAAAA;
    border: 1px solid #444444;
    padding: 2px;
  ]],

  tabActive = [[
    background-color: #4444AA;
    color: white;
    border: 1px solid #AAAAFF;
    font-weight: bold;
    padding: 2px;
  ]]
}


-- Container
MapUI.container = MapUI.container or Adjustable.Container:new({
  name = "mapUIContainer",
  titleText = "Map and Comms",
  x = "-25%", y = "0%",
  width = "25%", height = "50%",
})
MapUI.container:attachToBorder("right")


-- Tab bar
MapUI.tabBar = Geyser.HBox:new({
  name = "mapUIHBox",
  x = 0, y = 0,
  width = "100%", height = "4%",
}, MapUI.container)


-- Content areas
MapUI.views = {}

MapUI.views.map = Geyser.Label:new({
  name = "mapViewContainer",
  x = "0%", y = "5%",
  width = "100%", height = "95%",
}, MapUI.container)

MapUI.views.comms = Geyser.MiniConsole:new({
  name = "commsMini",
  autoWrap = true,
  x = "0%", y = "5%",
  width = "100%", height = "95%",
}, MapUI.container)

MapUI.views.misc = Geyser.MiniConsole:new({
  name = "miscMini",
  autoWrap = true,
  x = "0%", y = "5%",
  width = "100%", height = "95%",
}, MapUI.container)


-- Map Box
MapUI.mapBox = Geyser.Container:new({
  name = "MapBox",
  titleText = "Score Details",
  autoWrap = true,
  x = "0%", y = "5%",
  width = "100%", height = "100%",
}, MapUI.views.map)

MapUI.activeCommsMini = Geyser.MiniConsole:new({
  name = "activeCommsMini",
  autoWrap = true,
  x = "0%", y = "5%",
  width = "100%", height = "100%",
}, MapUI.views.comms)

for _, v in pairs({
  MapUI.mapBox,
  MapUI.views.comms,
  MapUI.views.misc,
}) do
  v:setColor("black")
end


-- Tab definitions
MapUI.tabs = {
  score = {
    label = "Map",
    view  = MapUI.views.map,
  },
  inItems = {
    label = "Comms",
    view  = MapUI.views.comms,
  },
  spells = {
    label = "Misc",
    view  = MapUI.views.misc,
  },
}


-- Tab on click function
function MapUI:showTab(tabName)
  for name, tab in pairs(self.tabs) do
    tab.view:hide()
    tab.button:setStyleSheet(self.styles.tabInactive)
  end

  local active = self.tabs[tabName]
  if not active then return end

  active.view:show()
  active.button:setStyleSheet(self.styles.tabActive)
end


-- Make tab buttons
for name, tab in pairs(MapUI.tabs) do
  tab.button = Geyser.Label:new({
    name = "tab_" .. name,
    message = ("<center>%s</center>"):format(tab.label),
  }, MapUI.tabBar)

  tab.button:setStyleSheet(MapUI.styles.tabInactive)
  
  tab.button:setClickCallback(function()
    MapUI:showTab(name)
  end)
end


-- Default state
MapUI:showTab("score")
