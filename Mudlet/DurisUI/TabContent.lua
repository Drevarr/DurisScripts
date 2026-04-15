--[[
TabPanel
Author: Drevarr
License: Public Domain

]]


TabPanel = TabPanel or {}

function TabPanel:new(def)
  local o = {}
  setmetatable(o, self)
  self.__index = self

  o.name    = def.name
  o.styles  = def.styles
  o.default = def.default
  o.tabs    = {}


  -- Container
  o.container = Adjustable.Container:new(def.container)

  if def.attach then
    o.container:attachToBorder(def.attach)
  end


  -- Tab bar
  o.tabHeight = def.tabHeight or "10px"

  o.tabBar = Geyser.HBox:new({
    name   = o.name .. "_HBox",
    x      = 0,
    y      = 0,
    width  = "100%",
    height = o.tabHeight,
  }, o.container)


  -- Content area
  o.view = Geyser.Label:new({
    name   = o.name .. "_View",
    x      = "0%",
    y      = o.tabHeight,
    width  = "100%",
    height = "95%",
  }, o.container)


  -- Tabs (factories)
  for key, tab in pairs(def.tabs) do
    -- Create view using factory
    local view = tab.create(o.view)
    view:hide()

    local button = Geyser.Label:new({
      name    = o.name .. "_Tab_" .. key,
      message = ("<center>%s</center>"):format(tab.label),
    }, o.tabBar)

    button:setStyleSheet(o.styles.tabInactive)
    button:setClickCallback(function()
      o:showTab(key)
    end)

    o.tabs[key] = {
      label  = tab.label,
      view   = view,
      button = button,
    }
  end


  -- Default tab
  o:showTab(o.default)

  return o
end

function TabPanel:showTab(tabName)
  for _, tab in pairs(self.tabs) do
    tab.view:hide()
    tab.button:setStyleSheet(self.styles.tabInactive)
  end

  local active = self.tabs[tabName]
  if not active then return end

  active.view:show()
  active.button:setStyleSheet(self.styles.tabActive)
end

