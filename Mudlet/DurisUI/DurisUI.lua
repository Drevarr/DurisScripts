--[[
Duris UI
Author: Drevarr
License: Public Domain

]]


DurisUI = DurisUI or {}
DurisUI.panels = {}

function DurisUI.getTab(panelName, tabName)
  local panel = DurisUI.panels[panelName]
  if not panel then return nil end

  local tab = panel.tabs[tabName]
  if not tab then return nil end

  return tab
end


function DurisUI.push(panelName, tabName, text, opts)
  opts = opts or {}

  local tab = DurisUI.getTab(panelName, tabName)
  if not tab or not tab.view then return end

  local view = tab.view

  if view.clear and opts.clear ~= false then
    view:clear()
  end

  if view.echo then
    view:echo(text)
  elseif view.setText then
    view:setText(text)
  end

  if opts.activate then
    DurisUI.panels[panelName]:showTab(tabName)
  end
end


function DurisUI.append(panelName, tabName, text)
  DurisUI.push(panelName, tabName, text, { clear = false })
end


function DurisUI.renderList(panelName, tabName, list, formatter)
  local tab = DurisUI.getTab(panelName, tabName)
  if not tab or not tab.view then return end

  local mini = tab.view
  mini:clear()

  if not list or #list == 0 then
    mini:echo("Nothing here.\n")
    return
  end

  for _, item in ipairs(list) do
    mini:echo(formatter(item) .. "\n")
  end
end


