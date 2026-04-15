GMCP = GMCP or {}

local function deepCopy(t)
  if type(t) ~= "table" then return t end
  local copy = {}
  for k, v in pairs(t) do
    copy[k] = deepCopy(v)
  end
  return copy
end

GMCP = GMCP or {}
GMCP.deepCopy = deepCopy

GMCP.store = function(namespace, data)
  GMCP[namespace] = GMCP[namespace] or { curr = {}, prev = {} }
  GMCP[namespace].prev = GMCP.deepCopy(GMCP[namespace].curr)
  GMCP[namespace].curr = data
end


