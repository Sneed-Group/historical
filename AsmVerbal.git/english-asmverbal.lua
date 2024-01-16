--English To AsmVerbal Translator
--by Samuel Lord
ABCU = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"}
abcl = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
numbers = {"0","1","2","3","4","5","6","7","8","9"}
punct = {".","?","!",","}
space = {" "}
asmCapsIndicator = "^"
asmLetter = {"11111111111111111111111111","1111111111111111111111111","111111111111111111111111","11111111111111111111111","1111111111111111111111","111111111111111111111","11111111111111111111","1111111111111111111","111111111111111111","11111111111111111","1111111111111111","111111111111111","11111111111111","1111111111111","111111111111","11111111111","1111111111","111111111","1111111","111111","11111","1111","111","11","1"}
asmNumbers = {"0","00","000","0000","00000","000000","0000000","00000000","000000000","0000000000"}
asmPunct = {"*PER*","*QUES*","*EXC*","*COM*"}
asmSpace = {"-"}
asmNewChar = "_"
print("FROM: ")
fromStr = io.read("*l")
output = ""
prevCharIsNumber = false
for i = 1, #fromStr do
    local char = fromStr:sub(i, i)
    for index,value in pairs(ABCU) do
        if char == value then
           output = output .. asmNewChar .. asmCapsIndicator .. asmLetter[index] 
           prevCharIsNumber = false
        end
    end
    for index,value in pairs(abcl) do
        if char == value then
           output = output .. asmNewChar .. asmLetter[index]
           prevCharIsNumber = false
        end
    end
    for index,value in pairs(punct) do
        if char == value then
           output = output .. asmPunct[index]
           prevCharIsNumber = false
        end
    end
    for index,value in pairs(space) do
        if char == value then
           output = output .. asmSpace[index]
           prevCharIsNumber = false
        end
    end
    for index,value in pairs(numbers) do
        if char == value then
            if prevCharIsNumber then
                output = output .. "/" .. asmNumbers[index]
            else
                output = output .. asmNewChar .. asmNumbers[index]
            end
            
            prevCharIsNumber = true
        end
    end
end
print(output)
