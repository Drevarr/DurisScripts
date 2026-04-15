--[[
In Room View Updater
Author: Drevarr
License: Public Domain

]]


InRoomUI.currentFriendlyAction = {
  LeftButton  = "Follow",
  RightButton = "Consent",
  MidButton   = "Group",
}

InRoomUI.currentEnemyAction = {
  LeftButton  = "kill",
  RightButton = "bash",
  MidButton   = "bodyslam",
}

InRoomUI.currentItemAction = {
  LeftButton  = "get",
  RightButton = "look",
  MidButton   = "hide",
}

InRoomUI.currentMobAction = {
  LeftButton  = "kill",
  RightButton = "look",
  MidButton   = "consider",
}


function InRoomUI:updateTabRows(tabName, dataList, displayKey, actions, hoverColor)
  local rowsKey = tabName .. "Rows"
  InRoomUI.widgets[rowsKey] = InRoomUI.widgets[rowsKey] or {}

  -- delete old rows
  for _, row in pairs(InRoomUI.widgets[rowsKey]) do
    deleteLabel(row.name)
  end
  InRoomUI.widgets[rowsKey] = {}

  if not dataList or #dataList == 0 then return end

  -- count duplicates by display key
  local counts = {}
  local entries = {}

  for _, obj in ipairs(dataList) do
    local baseName = obj[displayKey]
    if baseName then
      counts[baseName] = (counts[baseName] or 0) + 1
      local index = counts[baseName]

      local displayName = (index > 1)
        and (index .. "." .. baseName)
        or baseName

      table.insert(entries, {
        display = displayName,
        target  = obj.target, -- ALWAYS used for click actions
      })
    end
  end

  -- create labels
  for i, entry in ipairs(entries) do
    local labelName = string.format("InRoom_%sRow_%d", tabName, i)
    local parent = InRoomUI.widgets[tabName]

    local row = Geyser.Label:new({
      name   = labelName,
      x      = "0%",
      y      = (i - 1) * 22,
      width  = "100%",
      height = 22,
    }, parent)

    row:echo(entry.target)

    row:setStyleSheet(string.format([[
      QLabel {
        padding-left: 6px;
        color: #DDDDDD;
        background-color: transparent;
      }
      QLabel:hover {
        background-color: %s;
      }
    ]], hoverColor))

    setLabelClickCallback(labelName, function(event)
      local cmd = actions[event.button]
      if cmd and entry.target then
        send(cmd .. " " .. entry.display)
      end
    end)

    InRoomUI.widgets[rowsKey][i] = row
  end
end