--LibCrossplatformASM
--A minimal (while still somewhat usable modern day) cross-platform ASM re-imagining in LUA.
--By NodeMixaholic (SparksammyOfficial on ROBLOX)
---IS
--CHECKS IF 2 NUMBERS EQUAL
---GRT
--CHECKS IF N1 > N2
---LES
--CHECKS IF N1 < N2
---LOAD (LOAD: VAR,POS)
--Loads from VRAM
---STOR
--Saves to VRAM
---CLRR
--Clears VRAM
---ADD
--Adds 2 numbers
---SUB
---MULT
---DIV
---PRNT
--PRNT Hello, World 
---DEF (defines var)
---ASM (does crossplat asm)

local ram = {} --Our virtual RAM


function _G.ExecCrossplatASM(instruction)
	local indivIns = instruction.split("#/&")
	pcall(function()
		if (tostring(indivIns[1]).lower() == "is") then
			if (tonumber(indivIns[2]) == tonumber(indivIns[3])) then
				return true
			else
				return false
			end
		elseif (tostring(indivIns[1]).lower() == "grt") then
			if (tonumber(indivIns[2]) > tonumber(indivIns[3])) then
				return true
			else
				return false
			end
		elseif (tostring(indivIns[1]).lower() == "les") then
			if (tonumber(indivIns[2]) < tonumber(indivIns[3])) then
				return true
			else
				return false
			end
		elseif (tostring(indivIns[1]).lower() == "load") then
			_G.asmvar[indivIns[2]] = ram[tonumber(indivIns[3])]
		elseif (tostring(indivIns[1]).lower() == "stor") then	
			ram.insert(indivIns[2])
		elseif (tostring(indivIns[1]).lower() == "clrr") then	
			ram = {}
		elseif (tostring(indivIns[1]).lower() == "add") then
			return tonumber(indivIns[2]) + tonumber(indivIns[3])
		elseif (tostring(indivIns[1]).lower() == "sub") then	
			return tonumber(indivIns[2]) - tonumber(indivIns[3])
		elseif (tostring(indivIns[1]).lower() == "mult") then
			return tonumber(indivIns[2]) * tonumber(indivIns[3])
		elseif (tostring(indivIns[1]).lower() == "div") then
			return tonumber(indivIns[2]) / tonumber(indivIns[3])
		elseif (tostring(indivIns[1]).lower() == "def") then
			_G.asmvar[indivIns[2]] = indivIns[3]
		elseif (tostring(indivIns[1]).lower() == "prnt") then
			print(indivIns[2])
		elseif (tostring(indivIns[1]).lower() == "asm") then
			_G.ExecCrossplatASM(indivIns[2])
		end
	end)
end

print("LibCrossplatformASM for ROBLOX ready!")
