function castSpell(charClass, spellname, target, direction)
	local c = charClass
	local s = c[spellname]
	local t = target or false
	local d = direction or false
	if s and t and d then
		send("cast '"..s.."'"..t" "..d)	
	elseif s and t then
		send("cast '"..s.."'"..t)
	elseif s then
		send("cast '"..s.."'")
	else
		for k, v in pairs(c) do
			print(k , v)
		end
	end
end