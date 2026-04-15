GROUP_CMDS = GROUP_CMDS or {}

GROUP_CMDS = {
  ["LeftButton"] = {
    label = "Assist",
    action = function(member)
      send("assist " .. member)
    end
  },

  ["MidButton"] = {
    label = "Guard",
    action = function(member)
      send("guard " .. member)
    end
  },

  ["RightButton"] = {
    label = "Rescue",
    action = function(member)
      send("rescue " .. member)
    end
  },

  ["BackButton"] = {
    label = "Stone",
    action = function(member)
      send("cast 'stone' " .. member)
    end
  },
  ["ForwardButton"] = {
    label = "Globe",
    action = function(member)
      send("cast 'major globe' " .. member)
    end
  },
  ["TaskButton"] = nil,
  ["ExtraButton4"] = nil,
  ["ExtraButton5"] = nil,
  ["ExtraButton6"]  = nil,
  ["ExtraButton7"]  = nil,
  ["ExtraButton8"]  = nil,
  ["ExtraButton9"]  = nil,
  ["ExtraButton10"] = nil,
  ["ExtraButton11"] = nil,
  ["ExtraButton12"] = nil,
  ["ExtraButton13"] = nil,
  ["ExtraButton14"] = nil,
  ["ExtraButton15"] = nil,
  ["ExtraButton16"] = nil,
  ["ExtraButton17"] = nil,
  ["ExtraButton18"] = nil,
  ["ExtraButton19"] = nil,
  ["ExtraButton20"] = nil,
  ["ExtraButton21"] = nil,
  ["ExtraButton22"] = nil,
  ["ExtraButton23"] = nil,
  ["ExtraButton24"] = nil,
}


function Group_Grid_OnClick(member, event)
  local buttonName = event.button
  --echo("Clicked: " .. buttonName)
	local entry = GROUP_CMDS[buttonName]
	if entry and entry.action then
	  entry.action(member)
	end
end