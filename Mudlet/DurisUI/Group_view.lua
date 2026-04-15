--[[
Group View
Author: Drevarr
License: Public Domain

Example Usage:
cecho("GroupGrid", "<green>Group member joined!\n")
echo("GroupGrid", "Hello GroupGrid!\n")

]]


GroupUI = GroupUI or {}
GroupUI.widgets = GroupUI.widgets or {}

GroupUI.panel = TabPanel:new({
  name = "GroupUI",

  container = {
    name      = "groupUIContainer",
    titleText = "Group Data",
    x         = "-25%",
    y         = "50%",
    width     = "25%",
    height    = "50%",
  },

  attach    = "right",
  tabHeight = "5%",
  styles    = UIStyles,
  default   = "groupGrid",

  tabs = {

    groupGrid = {
      label = "GroupGrid",
      create = function(parent)
        GroupUI.widgets.groupGrid = Geyser.Label:new({
          name     = "groupGridLabel",
          autoWrap = true,
          x        = "0%", y = "0%",
          width    = "100%", height = "100%",
        }, parent)

        GroupUI.widgets.groupGrid:setColor("black")
        return GroupUI.widgets.groupGrid
      end
    },

    comms = {
      label = "GroupText",
      create = function(parent)
        GroupUI.widgets.groupText = Geyser.MiniConsole:new({
          name     = "groupTextMini",
          autoWrap = true,
          x        = "0%", y = "0%",
          width    = "100%", height = "100%",
        }, parent)

        GroupUI.widgets.groupText:setColor("black")
        return GroupUI.widgets.groupText
      end
    },

    misc = {
      label = "DualMode",
      create = function(parent)
        GroupUI.widgets.dualMode = Geyser.Container:new({
          name   = "dualModeContainer",
          x      = "0%", y = "0%",
          width  = "100%", height = "100%",
        }, parent)

        GroupUI.widgets.dualGrid = Geyser.Label:new({
          name     = "dualGridLabel",
          autoWrap = true,
          x        = "0%", y = "0%",
          width    = "100%", height = "50%",
        }, GroupUI.widgets.dualMode)
        GroupUI.widgets.dualGrid:setColor("black")

        GroupUI.widgets.dualMini = Geyser.MiniConsole:new({
          name   = "dualMiniConsole",
          x      = "0%", y = "50%",
          width  = "100%", height = "50%",
        }, GroupUI.widgets.dualMode)
        GroupUI.widgets.dualMini:setColor("green")

        return GroupUI.widgets.dualMode
      end
    },

  }
})

DurisUI.panels.GroupUI = GroupUI.panel