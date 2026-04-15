--[[
Map UI
Author: Drevarr
License: Public Domain

]]


MapUI = MapUI or {}
MapUI.widgets = MapUI.widgets or {}

MapUI.panel = TabPanel:new({
  name = "MapUI",

  container = {
    name      = "mapUIContainer",
    titleText = "Map and Comms",
    x         = "-25%",
    y         = "0%",
    width     = "25%",
    height    = "50%",
  },

  attach    = "right",
  tabHeight = "5%",
  styles    = UIStyles,
  default   = "map",

  tabs = {

    map = {
      label = "Map",
      create = function(parent)
        MapUI.widgets.mapContainer = Geyser.Container:new({
          name   = "mapView",
          x      = "0%", y = "0%",
          width  = "100%", height = "100%",
        }, parent)

        MapUI.widgets.mapBox = Geyser.Label:new({
          name   = "mapBox",
          x      = "0%", y = "0%",
          width  = "100%", height = "100%",
        }, MapUI.widgets.mapContainer)

        MapUI.widgets.mapBox:setColor("black")
        return MapUI.widgets.mapContainer
      end
    },

    comms = {
      label = "Comms",
      create = function(parent)
        MapUI.widgets.comms = Geyser.MiniConsole:new({
          name     = "commsMini",
          autoWrap = true,
          x        = "0%", y = "0%",
          width    = "100%", height = "100%",
        }, parent)

        MapUI.widgets.comms:setColor("black")
        return MapUI.widgets.comms
      end
    },

    misc = {
      label = "Misc",
      create = function(parent)
        MapUI.widgets.misc = Geyser.MiniConsole:new({
          name     = "miscMini",
          autoWrap = true,
          x        = "0%", y = "0%",
          width    = "100%", height = "100%",
        }, parent)

        MapUI.widgets.misc:setColor("black")
        return MapUI.widgets.misc
      end
    },

  }
})

DurisUI.panels.MapUI = MapUI.panel
