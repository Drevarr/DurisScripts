--[[
In Room View
Author: Drevarr
License: Public Domain

]]

InRoomUI = InRoomUI or {}
InRoomUI.widgets = InRoomUI.widgets or {}

InRoomUI.panel = TabPanel:new({
  name = "InRoomUI",

  container = {
    name      = "inRoomContainer",
    titleText = "In Room",
    x         = "0%",
    y         = "60%",
    width     = "15%",
    height    = "40%",
  },

  attach    = "left",
  tabHeight = "20px",
  styles    = UIStyles,
  default   = "players",

  tabs = {

    mobs = {
      label = "Mobs",
      create = function(parent)
        InRoomUI.widgets.mobs = Geyser.Label:new({
          name   = "InRoomMobsView",
          x      = "0%", y = "0%",
          width  = "100%", height = "100%",
        }, parent)
    
        InRoomUI.widgets.mobsRows = {}
        InRoomUI.widgets.mobs:setColor('black')
        return InRoomUI.widgets.mobs

      end
    },

    items = {
      label = "Items",
      create = function(parent)
        InRoomUI.widgets.items = Geyser.Label:new({
          name     = "InRoomItemsView",
          autoWrap = true,
          x        = "0%", y = "0%",
          width    = "100%", height = "100%",
        }, parent)

        InRoomUI.widgets.itemsRows = {}
        InRoomUI.widgets.items:setColor("black")
        return InRoomUI.widgets.items
      end
    },

    players = {
      label = "Players",
      create = function(parent)
        InRoomUI.widgets.players = Geyser.Label:new({
          name     = "InRoomPlayerView",
          autoWrap = true,
          x        = "0%", y = "0%",
          width    = "100%", height = "100%",
        }, parent)

        InRoomUI.widgets.playersRows = {}
        InRoomUI.widgets.players:setColor("black")
        return InRoomUI.widgets.players
      end
    },

  }
})

DurisUI.panels.InRoomUI = InRoomUI.panel