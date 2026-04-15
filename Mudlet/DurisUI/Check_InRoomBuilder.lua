-- Generalized row builder for InRoomUI tabs with exact-click targeting
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
