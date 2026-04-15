--[[
Character UI
Author: Drevarr
License: Public Domain

Example usge:
CharacterUI.widgets.stats:clear()
CharacterUI.widgets.stats:echo("<white>STR: 18  DEX: 17  CON: 19\n")
CharacterUI.widgets.affects:echo("<green>fly (65s)\n")
CharacterUI.widgets.skills:echo("Backstab 92%\n")
]]


CharacterUI = CharacterUI or {}
CharacterUI.widgets = CharacterUI.widgets or {}

CharacterUI.panel = TabPanel:new({
  name = "CharacterUI",

  container = {
    name      = "characterUIContainer",
    titleText = "Character",
    x         = "0%",
    y         = "0%",
    width     = "15%",
    height    = "70%",
  },

  attach    = "left",
  tabHeight = "20px",
  styles    = UIStyles,
  default   = "stats",

  tabs = {

    stats = {
      label = "Stats",
      create = function(parent)
        CharacterUI.widgets.stats = Geyser.MiniConsole:new({
          name     = "statsMini",
          autoWrap = true,
          x        = "0%", y = "0%",
          width    = "100%", height = "100%",
        }, parent)

        CharacterUI.widgets.stats:setColor("black")
        return CharacterUI.widgets.stats
      end
    },

    affects = {
      label = "Affects",
      create = function(parent)
        CharacterUI.widgets.affects = Geyser.MiniConsole:new({
          name     = "affectsMini",
          autoWrap = true,
          x        = "0%", y = "0%",
          width    = "100%", height = "100%",
        }, parent)

        CharacterUI.widgets.affects:setColor("black")
        return CharacterUI.widgets.affects
      end
    },

    skills = {
      label = "Spells|Skills",
      create = function(parent)
        CharacterUI.widgets.skills = Geyser.MiniConsole:new({
          name     = "skillsMini",
          autoWrap = true,
          x        = "0%", y = "0%",
          width    = "100%", height = "100%",
        }, parent)

        CharacterUI.widgets.skills:setColor("black")
        return CharacterUI.widgets.skills
      end
    },

  }
})

DurisUI.panels.CharacterUI = CharacterUI.panel
