--[[
Format Comma Value Numbers
Author: Drevarr
License: Public Domain

]]


function comma_value(amount)
    -- Convert the number to a string and ensure it's an integer part for comma separation
    local formatted = string.format('%.0f', amount)
    local k
    while true do
        -- Substitute the pattern of an optional minus sign, followed by 
        -- one or more digits, and then exactly three digits. Inserts a comma.
        formatted, k = string.gsub(formatted, "^(-?%d+)(%d%d%d)", '%1,%2')
        -- If no substitution occurred (k==0), break the loop
        if (k == 0) then
            break
        end
    end
    return formatted
end