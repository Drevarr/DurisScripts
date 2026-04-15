function InRoomUI:updateTabRows(tabName, dataList, displayKey, actions, hoverColor)
  InRoomUI.widgets[tabName .. "Rows"] = InRoomUI.widgets[tabName .. "Rows"] or {}

  -- Delete old rows
  for _, row in pairs(InRoomUI.widgets[tabName .. "Rows"]) do
    deleteLabel(row.name)
  end
  InRoomUI.widgets[tabName .. "Rows"] = {}

  if not dataList or #dataList == 0 then return end

  -- Count duplicates for the display name
  local counts = {}
  local displayList = {}
  for _, obj in ipairs(dataList) do
    local key = obj[displayKey]
    counts[key] = (counts[key] or 0) + 1
    local index = counts[key]

    local displayName
    if index > 1 then
      displayName = index .. "." .. key
    else
      displayName = key
    end

    table.insert(displayList, {
      display = displayName,  -- shown on label
      target  = displayName,  -- used in click callback
    })
  end

  -- Create labels
  for i, entry in ipairs(displayList) do
    local labelName = string.format("InRoom_%sRow_%d", tabName, i)
    local parent = InRoomUI.widgets[tabName]
    local row = Geyser.Label:new({
      name   = labelName,
      x      = "0%",
      y      = (i - 1) * 22,
      width  = "100%",
      height = 22,
    }, parent)

    row:echo(entry.display)
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

    -- Click callback uses displayName as target
    setLabelClickCallback(labelName, function(event)
      local cmd = actions[event.button]
      if cmd then
        send(cmd .. " " .. entry.target)
      end
    end)

    InRoomUI.widgets[tabName .. "Rows"][i] = row
  end
end


function InRoomUI:populateMobsFromGMCP()
  local npcs = gmcp.Room.Info.npcs
  if not npcs or #npcs == 0 then
    InRoomUI:updateMobs({})
    return
  end

  -- Build a table keyed by keyword, counting duplicates
  local keywordCounts = {}
  local displayList = {}

  for _, npc in ipairs(npcs) do
    local key = npc.keyword
    keywordCounts[key] = (keywordCounts[key] or 0) + 1
    local count = keywordCounts[key]

    local displayName
    if count > 1 then
      displayName = count .. "." .. key
    else
      displayName = key
    end

    -- store both displayName and keyword for click
    table.insert(displayList, {
      display = displayName,
      target  = key
    })
  end

  -- Convert to the format InRoomUI:updateMobs expects
  local mobRows = {}
  for _, mob in ipairs(displayList) do
    table.insert(mobRows, {
      name   = mob.display,
      target = mob.target
    })
  end

  -- Custom updater that passes keyword to onclick
  InRoomUI.widgets.mobsRows = InRoomUI.widgets.mobsRows or {}

  -- delete old rows
  for _, row in pairs(InRoomUI.widgets.mobsRows) do
    deleteLabel(row:getName())
  end
  InRoomUI.widgets.mobsRows = {}

  -- create new rows
  for i, mob in ipairs(mobRows) do
    local labelName = "InRoom_MobRow_" .. i

    local row = Geyser.Label:new({
      name   = labelName,
      x      = "0%",
      y      = (i - 1) * 22,
      width  = "100%",
      height = 22,
    }, InRoomUI.widgets.mobs)

    row:setText(mob.name)
    row:setStyleSheet([[
      QLabel {
        padding-left: 6px;
        color: #DDDDDD;
        background-color: transparent;
      }
      QLabel:hover {
        background-color: #552222;
      }
    ]])

    setLabelClickCallback(labelName, function(event)
      local cmd = InRoomUI.currentMobAction[event.button]
      if cmd then
        send(cmd .. " " .. mob.target)
      end
    end)

    InRoomUI.widgets.mobsRows[i] = row
  end
end