--RoboLang Sparksammy Mystery Rewrite Edition FILE LOADER
--I had 0 look at the source code of RoboCode, but knew what it did early on.
--So I worked on a "Mystery ReWrite" that I showed only very early progress and when it was finished on to Oklomsy, the creator.
--Credit to him for the creation of RoboCode BTW.

local open = io.open

args = {}

for line in io.lines(...) do

function wait(seconds)
	local start = os.time()
	repeat until os.time() > start + seconds
end
for token in string.gmatch(line, "[^%s]+") do
	table.insert(args, token)
	wait(.3)
	for i,ln in ipairs(args) do
		if ln == "beep" or ln == "boop" or ln == "bap" or ln == "boap" then
			table.remove(args, 1)
			_G.cmd = ln	  
		end
		end
		end
		if _G.cmd == "boop" then
			if args[1] > args[2] then
				print(args[1] .. " is greater")
			elseif args[1] < args[2] then
				print(args[2] .. " is greater")
			end
		elseif _G.cmd == "bap" then
			if args[1] < args[2] then
				print(args[1] .. " is less")
			elseif args[1] > args[2] then
				print(args[2] .. " is less")
			end
		elseif _G.cmd == "boap" then
			if args[1] == args[2] then
				print(args[1] .. " is equal to: " .. args[2])
			elseif args[1] ~= args[2] then
				print(args[1] .. " is NOT equal to: " .. args[2])
			end
		elseif _G.cmd == "beep" then
			for argu,arguline in ipairs(args) do
				io.write(arguline .. " ")
			end
end 
args = {} --clean up
end
