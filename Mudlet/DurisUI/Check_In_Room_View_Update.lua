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


function InRoomUI:prepareDisplayList(dataList, keyField)
  local counts = {}
  local displayList = {}

  for _, obj in ipairs(dataList) do
    local key = obj[keyField]
    counts[key] = (counts[key] or 0) + 1
    local index = counts[key]

    local displayName = (index > 1) and (index .. "." .. key) or key

    table.insert(displayList, {
      display = displayName,  -- shown on label
      target  = displayName,  -- used in click callback
    })
  end

  return displayList
end


function InRoomUI.onMobClick(event, mobName)
  local cmd = InRoomUI.currentMobAction[event.button]
  if cmd then
    send(cmd .. " " .. mobName)
  end
end

function InRoomUI.onItemClick(event, itemName)
  local cmd = InRoomUI.currentItemAction[event.button]
  if cmd then
    send(cmd .. " " .. itemName)
  end
end

function InRoomUI.onFriendlyClick(event, friendlyName)
  local cmd = InRoomUI.currentFriendlyAction[event.button]
  if cmd then
    send(cmd .. " " .. friendlyName)
  end
end

function InRoomUI.onEnemyClick(event, enemyName)
  local cmd = InRoomUI.currentEnemyAction[event.button]
  if cmd then
    send(cmd .. " " .. enemyName)
  end
end


InRoomUI.rowTypes = {

  mob = {
    container = "mobs",
    actions   = function() return InRoomUI.currentMobAction end,
    onClick   = InRoomUI.onMobClick,
    hoverBg   = "#552222",
  },

  item = {
    container = "items",
    actions   = function() return InRoomUI.currentItemAction end,
    onClick   = InRoomUI.onItemClick,
    hoverBg   = "#225522",
  },

  friendly = {
    container = "players",
    actions   = function() return InRoomUI.currentFriendlyAction end,
    onClick   = InRoomUI.onFriendlyClick,
    hoverBg   = "#224488",
  },

  enemy = {
    container = "players",
    actions   = function() return InRoomUI.currentEnemyAction end,
    onClick   = InRoomUI.onEnemyClick,
    hoverBg   = "#882222",
  },
}

function InRoomUI:createRow(rowType, index, name)
  local cfg = InRoomUI.rowTypes[rowType]
  if not cfg then return end

  local labelName = string.format("InRoom_%sRow_%d", rowType, index)

  local parent = InRoomUI.widgets[cfg.container]

  local row = Geyser.Label:new({
    name   = labelName,
    x      = "0%",
    y      = (index - 1) * 22,
    width  = "100%",
    height = 22,
  }, parent)

  row:echo(name)

  row:setStyleSheet(string.format([[
    QLabel {
      padding-left: 6px;
      color: #DDDDDD;
      background-color: transparent;
    }
    QLabel:hover {
      background-color: %s;
    }
  ]], cfg.hoverBg))

  setLabelClickCallback(labelName, function(event)
    cfg.onClick(event, name)
  end)

  return row
end


function InRoomUI:updateMobs(mobList)
  InRoomUI.widgets.mobsRows = InRoomUI.widgets.mobsRows or {}
  for _, row in pairs(InRoomUI.widgets.mobsRows) do
    deleteLabel(row.name)
  end
  InRoomUI.widgets.mobsRows = {}

  local displayList = InRoomUI:prepareDisplayList(mobList, "keyword")

  for i, mob in ipairs(displayList) do
    InRoomUI.widgets.mobsRows[i] =
      InRoomUI:createRow("mob", i, mob.target)  -- pass the displayName as name
  end
end

function InRoomUI:updateItems(itemList)
  InRoomUI.widgets.itemsRows = InRoomUI.widgets.itemsRows or {}
  for _, row in pairs(InRoomUI.widgets.itemsRows) do
    deleteLabel(row.name)
  end
  InRoomUI.widgets.itemsRows = {}

  local displayList = InRoomUI:prepareDisplayList(itemList, "name")

  for i, item in ipairs(displayList) do
    InRoomUI.widgets.itemsRows[i] =
      InRoomUI:createRow("item", i, item.target)
  end
end

function InRoomUI:updatePlayers(friendlies, enemies)
  InRoomUI.widgets.playerRows = InRoomUI.widgets.playerRows or {}
  for _, row in pairs(InRoomUI.widgets.playerRows) do
    deleteLabel(row.name)
  end
  InRoomUI.widgets.playerRows = {}

  local i = 1
  local displayList

  -- Friendlies
  displayList = InRoomUI:prepareDisplayList(friendlies, "name")
  for _, p in ipairs(displayList) do
    InRoomUI.widgets.playerRows[i] =
      InRoomUI:createRow("friendly", i, p.target)
    i = i + 1
  end

  -- Enemies
  displayList = InRoomUI:prepareDisplayList(enemies, "name")
  for _, p in ipairs(displayList) do
    InRoomUI.widgets.playerRows[i] =
      InRoomUI:createRow("enemy", i, p.target)
    i = i + 1
  end
end