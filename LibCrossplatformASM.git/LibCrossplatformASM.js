//LibCrossplatformASM
//A minimal (while still somewhat usable modern day) cross-platform ASM re-imagining in LUA.
//By NodeMixaholic (SparksammyOfficial on ROBLOX)
///IS
//CHECKS IF 2 NUMBERS EQUAL
///GRT
//CHECKS IF N1 > N2
///LES
//CHECKS IF N1 < N2
///LOAD (LOAD: VAR,POS)
//Loads from VRAM
///STOR
//Saves to VRAM
///CLRR
//Clears VRAM
///ADD
//Adds 2 numbers
///SUB
///MULT
///DIV
///PRNT
// PRNT Hello, World 
///DEF (defines var)
///ASM (does crossplat asm)

let ram = [] //Our virtual RAM
let cpAsmVars = {};
function ExecCrossplatASM(instruction) {
    let ret = []
	try {
        let ins = instruction.split(";;")
        for (let i = 0; i < ins.length; i++) { 
        let indivIns = ins[i].split("#/&")
        if (String(indivIns[0]).toLowerCase() == "is") {
			if (Number(indivIns[1]) == Number(indivIns[2])) {
				ret.push(true)
			} else {
				ret.push(false)
			}
		} else if (String(indivIns[0]).toLowerCase() == "grt") {
			if (Number(indivIns[1]) > Number(indivIns[2])) {
				ret.push(true)
			} else {
				ret.push(false)
			}
		} else if (String(indivIns[0]).toLowerCase() == "les") {
			if (Number(indivIns[1]) < Number(indivIns[2])) {
				ret.push(true)
			} else {
				ret.push(false)
			}
		} else if (String(indivIns[0]).toLowerCase() == "load") {
			cpAsmVars[indivIns[1]] = ram[Number(indivIns[2])]
		} else if (String(indivIns[0]).toLowerCase() == "stor") {	
			ram.push(indivIns[2])
		} else if (String(indivIns[0]).toLowerCase() == "clrr") {	
			ram = []
		} else if (String(indivIns[0]).toLowerCase() == "add") {
			ret.push(Number(indivIns[1]) + Number(indivIns[2]))
		} else if (String(indivIns[0]).toLowerCase() == "sub") {	
			ret.push(Number(indivIns[1]) - Number(indivIns[2]))
		} else if (String(indivIns[0]).toLowerCase() == "mult") {
			ret.push(Number(indivIns[1]) * Number(indivIns[2]))
		} else if (String(indivIns[0]).toLowerCase() == "div") {
			ret.push(Number(indivIns[1]) / Number(indivIns[2]))
		} else if (String(indivIns[0]).toLowerCase() == "def") {
			cpAsmVars[indivIns[1]] = indivIns[2]
		} else if (String(indivIns[0]).toLowerCase() == "asm") {
			ExecCrossplatASM(indivIns[1])
		}
        }
        return ret;
	} catch (error) {
        console.log(`oh no! an error!
        details for devs:
        ${error}`)
    }
}

console.log("LibCrossplatformASM ready! By NodeMixaholic. Try this to test: ExecCrossplatASM(`is#/&1#/&1;;is#/&1#/&2`)")
