import builtins

class Parser:
    def __init__(self, code: str):
        #Pass in code
        self.code = code
        #Parse code
        self.code = self.Parse(self.code)

    def Parse(self, code: str) -> str:
        code = self.ParseComments(code)
        code = self.ParseInclude(code)
        code = self.ParseKeyWords(code)
        code = self.ParseEOL(code)
        code = self.ParseBraces(code)
        code = self.ParseFunctions(code)
        code = self.CleanCode(code)
        code = self.AddEntryPoint(code)

        #Dump code to file
        with open("output.py", "w") as f:
            f.write(code)
        return code
    def ParseComments(self, code: str) -> str:
        for line in code.splitlines():
            if "#" in line:
                if not self.IsInString("#", line):
                    if list(line)[0] == "#":
                        code = code.replace(line, "")
                    else:
                        newLine = line.partition("#")[0]
                        code = code.replace(line, newLine)                    
        return code

    def ParseInclude(self, code: str) -> str:
        includeName = ""
        # include-all *
        for line in code.splitlines():
            words = line.split()
            for wordNo, word in enumerate(words):
                if words[wordNo] == "include-all" and not self.IsInString(words[wordNo], line):
                            code = code.replace(line, f"from {words[wordNo + 1]} import *")
        # native-include path/to/lib.pyta
        for line in code.splitlines():
            words = line.split()
            for wordNo, word in enumerate(words):
                if word == "native-include" and not self.IsInString(word, line):
                    includeName = words[wordNo + 1]
                    code = code.replace(line, "")
                    with open(includeName.removesuffix(";") + ".pyta", "r") as file:
                        code = file.read() + "\n" + code
        # include * from **
        for line in code.splitlines():
            words = line.split()
            for wordNo, word in enumerate(words):
                if words[wordNo] == "include" and not self.IsInString(words[wordNo], line):
                        try:
                            if words[wordNo + 2] == "from":
                                code = code.replace(line, f"from {words[wordNo + 3]} import {words[wordNo + 1]}")
                        except IndexError:
                            code = code.replace(line, f"import {words[wordNo + 1]}")


        return code

    def ParseKeyWords(self, code: str) -> str:
        for line in code.splitlines():
            if "this" in line and not self.IsInString("this", line):
                code = code.replace(line, line.replace("this", "self"))
        for line in code.splitlines():
            if "true" in line and not self.IsInString("true", line):
                code = code.replace(line, line.replace("true", "True"))
        for line in code.splitlines():
            if "false" in line and not self.IsInString("false", line):
                code = code.replace(line, line.replace("false", "False"))
        for line in code.splitlines():
            if "null" in line and not self.IsInString("null", line):
                code = code.replace(line, line.replace("null", "None"))
        for line in code.splitlines():
            if "else if" in line and not self.IsInString("else if", line):
                code = code.replace(line, line.replace("else if", "elif"))
        for line in code.splitlines():
            if "console.writeLine" in line and not self.IsInString("console.writeLine", line):
                code = code.replace(line, line.replace("console.writeLine", "print"))
        return code

    def ParseEOL(self, code: str) -> str:
        code = "".join([s for s in code.splitlines(True) if s.strip("\r\n")])

        for line in code.splitlines():
            skipLine = False
            for token in ("role", "while", "for", "if", "else", "elif", "with", "from"):
                if token in line and not self.IsInString(token, line):
                    skipLine = True
            if ''.join(line.split()).startswith(("{", "}", "\n", "group")):
                skipLine = True
            elif line.strip() == "":
                skipLine = True
            if skipLine:
                continue

        return code

        newCode = ""
        splitLines = code.splitlines();
        for line in splitLines:
            if ";" in line and not self.IsInString(";", line):
                lineChars = list(line)
                stringCount = 0
                for i in range(len(lineChars)):
                    if lineChars[i] == '"' or lineChars[i] == "'":
                        stringCount += 1
                    if lineChars[i] == ";":
                        if stringCount % 2 == 0:
                            lineChars[i] = "\n"
                            break
                line = "".join(lineChars)
            if "group" in line:
                if not self.IsInString("group", line):
                    line = "\n"+" ".join(line.split())
                    line = line.replace("group", "class")
            if "role" in line:
                if line.partition("role")[0].count("\"") != 0 and line.partition("role")[0].count("\"") % 2 == 0:
                    words = line.split()
                    for wordNo, word in enumerate(words):
                        if word == "role":
                            speechCount = line.partition("role")[2].count("\"")
                            otherCount = line.partition("role")[2].count("'")
                            if speechCount % 2 == 0 and otherCount % 2 == 0:
                                words[wordNo] = "def"
                                break
                    line = " ".join(words)
            leftBraceExpression = ''.join(line.split())
            if not self.IsInString("{", leftBraceExpression):
                if ''.join(line.split()).startswith(("{")):
                    newCode += ":\n"
            if not self.IsInString("}", line):
                    line = line.replace("}", "#endindent")
            if not self.IsInString("{", line):
                line = line.replace("{", "#startindent")
            line += "\n"
            newCode += line
            line += "\n"

        return newCode

    def ParseBraces(self, code: str) -> str:
        leftBracesAmount = 0
        for line in code.splitlines():
            if "{" in line:
                lineChars = list(line)
                stringCount = 0
                for i in range(len(lineChars)):
                    if lineChars[i] == '"' or lineChars[i] == "'":
                        stringCount += 1
                    if lineChars[i] == "{":
                        if stringCount % 2 == 0 and stringCount != 0:
                            leftBracesAmount += 1
                            break
        rightBracesAmount = 0
        for line in code.splitlines():
            if "}" in line:
                lineChars = list(line)
                stringCount = 0
                for i in range(len(lineChars)):
                    if lineChars[i] == '"' or lineChars[i] == "'":
                        stringCount += 1
                    if lineChars[i] == "}":
                        if stringCount % 2 == 0 and stringCount != 0:
                            rightBracesAmount += 1
                            break

        if leftBracesAmount != rightBracesAmount:
            print("Braces amount is not equal")

        newCode = ""
        splitLines = code.splitlines();
        for line in splitLines:
            if ";" in line and not self.IsInString(";", line):
                lineChars = list(line)
                stringCount = 0
                for i in range(len(lineChars)):
                    if lineChars[i] == '"' or lineChars[i] == "'":
                        stringCount += 1
                    if lineChars[i] == ";":
                        if stringCount % 2 == 0:
                            lineChars[i] = "\n"
                            break
                line = "".join(lineChars)
            if "group" in line:
                if not self.IsInString("group", line):
                    line = "\n"+" ".join(line.split())
                    line = line.replace("group", "class")
            if "function" in line:
                if line.partition("function")[0].count("\"") != 0 and line.partition("function")[0].count("\"") % 2 == 0:
                    words = line.split()
                    for wordNo, word in enumerate(words):
                        if word == "function":
                            speechCount = line.partition("function")[2].count("\"")
                            otherCount = line.partition("function")[2].count("'")
                            if speechCount % 2 == 0 and otherCount % 2 == 0:
                                words[wordNo] = "def"
                                break
                    line = " ".join(words)
            leftBraceExpression = ''.join(line.split())
            if not self.IsInString("{", leftBraceExpression):
                if ''.join(line.split()).startswith(("{")):
                    newCode += ":\n"
            if not self.IsInString("}", line):
                    line = line.replace("}", "#endindent")
            if not self.IsInString("{", line):
                line = line.replace(" {", ":")
            line += "\n"
            newCode += line
            line += "\n"

        return newCode


    def ParseFunctions(self, code: str) -> str:
        code = code
        for line in code.splitlines():
            if "role" in line and not self.IsInString("role", line):
                for line in code.splitlines():
                    words = line.split()
                    for wordNo, word in enumerate(words):
                        if words[wordNo] != "import" or words[wordNo] != "from":
                            code = code.replace(line, line.replace("role", "def"))
        return code

    def CleanCode(self, code : str) -> str:
        #I'm not going to lie, I made a lot of mistakes. Let's hope these hacks fix it.

        splitLines = code.splitlines()
        for lineNo, line in enumerate(splitLines):
            if line.startswith(":"):
                splitLines[lineNo - 1] = splitLines[lineNo - 1] + ":"
                splitLines[lineNo] = ""
        newCode = ""
        for line in splitLines:
            newCode += line + "\n"
        code = newCode

        splitLines = code.splitlines()
        newCode = ""
        for lineNo, line in enumerate(splitLines):
            i = 0
            indentCount = 0
            while i <= lineNo:
                if "#endindent" in splitLines[i]:
                    if not self.IsInString("#endindent", splitLines[i], True):
                        indentCount -= 1
                    
                elif "#startindent" in splitLines[i] and not self.IsInString("#startindent", splitLines[i], True):
                    if not self.IsInString("#startindent", splitLines[i]):
                        indentCount += 1
                i += 1
            newCode += ("    " * indentCount) + line + "\n"
        code = newCode

        #Tidy code by removing empty lines
        newCode = ""
        for line in code.splitlines():
            if line.strip("\t\r\n") == "":
                line = line.replace(line, line.strip("\t\r\n"))
                newCode += line
            else:
                newCode += line + "\n"
        code = newCode

        code = "\n".join([ll.rstrip() for ll in code.splitlines() if ll.strip()])

        return code

    def AddEntryPoint(self, code: str) -> str:
        code += "\n"
        code += '''
if __name__ == "__main__":
    Main.onRun()
        '''

        return code

    def IsInString(self, phrase : str, line : str, returnIfMultiple = False) -> bool:
        if not phrase in line:
            return False
        if line.count(phrase) > 1:
            return returnIfMultiple
        leftSide = line.partition(phrase)[0]
        if leftSide.count("\"") > 0:
            if leftSide.count("\"") % 2 == 0:
                return False
            else:
                return True
        if leftSide.count("\'") > 0:
            if leftSide.count("\'") % 2 == 0:
                return False
            else:
                return True
            
def getPyeta(code):
    parsed = Parser(code)
    return parsed.code

builtins.getPyeta = getPyeta
