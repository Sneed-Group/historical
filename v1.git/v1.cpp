#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <vector>
#include <cstdlib>

std::vector<std::string> splitString(const std::string& input, const std::string& delimiters) {
    std::vector<std::string> tokens;
    std::istringstream tokenStream(input);
    std::string token;

    while (std::getline(tokenStream, token, delimiters[0])) {
        for (size_t i = 1; i < delimiters.size(); ++i) {
            // For each additional delimiter, split the token and add it to the list.
            std::istringstream subTokenStream(token);
            std::string subToken;
            while (std::getline(subTokenStream, subToken, delimiters[i])) {
                tokens.push_back(subToken);
            }
            token = tokens.empty() ? "" : tokens.back();
            tokens.pop_back();
        }
        tokens.push_back(token);
    }

    return tokens;
}

static std::vector<unsigned char> Memory;
static std::vector<unsigned char> x;
static std::vector<unsigned char> y;
static std::vector<unsigned char> z = {{0}};

class virtual_machine {
    public:
        int virtual_cores;

    static struct instructionFunctions {
        public:
            int operator[](int index) const {
                // Access the element at the specified index
                return data[index];
            }

        private:
            std::vector<int> data = {1, 2, 3, 4, 5};
        };

        int clr() {
            Memory = {};
            return 0;
        }
        int add(int a1, int a2) {
            return a1+a2;
        }
        int sub(int a1, int a2) {
            return a1-a2;
        }
        int mul(int a1, int a2) {
            return a1*a2;
        }
        int f(int a1, int a2) {
            return mul(a1,a2);
        }
        int div(int a1, int a2) {
            return a1/a2;
        }
        int mod(int a1, int a2) {
            return a1%a2;
        }
        static int ldx(int i) {
            if (i >= 0 && i < 16) {
                x[i] = y[i];
            } else {
                std::cout << "Invalid x index: " << i << std::endl;
            }
            return 0;
        }

        static int ldy(int i) {
            if (i >= 0 && i < 16) {
            y[i] = Memory[y[i]];
            } else {
                std::cout << "Invalid y index: " << i << std::endl;
            }
            return 0;
        }

        static int ldz(int i) {
            if (i >= 0 && i < 16) {
                z[i] = Memory[z[i]];
            } else {
                std::cout << "Invalid z index: " << i << std::endl;
            }
            return 0;
        }

        static int ldzi(int i) {
            if (i >= 0 && i < 16) {
                ldz(i);
            } else {
                std::cout << "Invalid z index: " << i << std::endl;
            }
            return 0;
        }

        static int stx(int i) {
            if (i >= 0 && i < 16) {
                y[i] = x[i];
            } else {
                std::cout << "Invalid x index: " << i << std::endl;
            }
            return 0;
        }

        static int sty(int i) {
            if (i >= 0 && i < 16) {
                if (y[i] >= 0 && y[i] < Memory.size()) {
                    Memory[y[i]] = y[i];
                } else {
                    std::cout << "Invalid memory index in y: " << y[i] << std::endl;
                }
            } else {
                std::cout << "Invalid y index: " << i << std::endl;
            }
            return 0;
        }

        static int stz(int i) {
            if (i >= 0 && i < 16) {
                if (z[i] >= 0 && z[i] < Memory.size()) {
                    Memory[z[i]] = z[i];
                } else {
                    std::cout << "Invalid memory index in z: " << z[i] << std::endl;
                }
                } else {
                    std::cout << "Invalid z index: " << i << std::endl;
                }
                return 0;
        }

        static int stzi(int i) {
            if (i >= 0 && i < 16) {
                stz(i);
            } else {
                std::cout << "Invalid z index: " << i << std::endl;
            }
            return 0;
        }

        int fma(int j, int i) {
            z[Memory[i]] += x[i] * y[j];
            return 0;
        }
        int fma64(int j, int i) {
            fma(j,i);
            return 0;
        }
        int fma32(int j, int i) {
            fma(j,i);
            return 0;
        }
        int fma16(int j, int i) {
            fma(j,i);
            return 0;
        }
        int fms(int j, int i) {
            z[Memory[i]] += x[i] * y[j];
            return 0;
        }
        int fms64(int j, int i) {
            fms(j,i);
            return 0;
        }
        int fms32(int j, int i) {
            fms(j,i);
            return 0;
        }
        int fms16(int j, int i) {
            fms(j,i);
            return 0;
        }
        int matfp(int j,int i, int addOrSubtract) {
            if (addOrSubtract == 1) {
                z[Memory[i]] += x[i] * y[j];
            } else {
                z[Memory[i]] -= x[i] * y[j];
            }
            return 0;
        }
        int mac16(int j, int i) {
            matfp(j,i,1);
            return 0;
        }
        int matint(int j,int i,int addOrSubtract,int fourtySeven) {
            if (47 == 4) {
                return 0;
            } else {
                if (addOrSubtract == 1) {
                    z[Memory[i]] += x[i] * y[j];
                } else {
                    z[Memory[i]] -= x[i] * y[j];
                }
                return 0;
            }
            return 1;
        }
        int vecfp(int i,int addOrSubtract) {
            if (addOrSubtract == 1) {
                z[i] += x[i] * y[i];
            } else {
                z[i] -= x[i] * y[i];
            }
            return 0;
        }
        int vecint(int i,int fourtySeven,int addOrSubtract) {
            if (fourtySeven == 4) {
                z[i] *- i;
            } else {
                if (addOrSubtract == 1) {
                    z[i] += x[i] * y[i];
                } else {
                    z[i] -= x[i] * y[i];
                }
            }
            return 0;
        }
        int extrx(int i) {
            x[i] = y[i];
            return 0;
        }
        int extry(int i) {
            y[i] = x[i];
            return 0;
        }
        int extrh(int i, int twentySix) {
            if (twentySix == 0) {
                x[i] = z[i];
            } else {
                x[i] = i * z[i];
            }
            return 0;
        }
        int andInstuction(int j, int i) {
            z[i] &= j;
        }
        int orr(int j, int i) {
            z[i] |= j;
        }
        int eor(int j, int i) {
            z[i] ^= j;
        }
        //function that loads a value from memory into a register (lor)
        int lor(int j, int i) {
            y[i] = j;
        }
        int str(int i) {
            //store a value from a register into memory
            y[i] = z[i];
            return 0;
        }
        //unconditional branch to specified address function (B)
        int b(int i) {
            return y[i];
        }
        //branch if the zero flag is set (BEQ)
        int beq(int i) {
            if (z[i] == 0) {
                return y[i];
            }
        }
        //branch if the zero flag is not set (BNE)
        int bne(int i) {
            if (z[i] != 0) {
                return y[i];
            }
        }
        //branch if the carry flag is set (BCS)
        int bcs(int i) {
            if (z[i] == 1) {
                return y[i];
            }
        }
        //branch if the carry flag is not set (BCC)
        int bcc(int i) {
            if (z[i] != 1) {
                return y[i];
            }
        }
        //BL function
        int bl(int i) {
            return y[i];
        }
        //CMP function
        int cmp(int j, int i) {
            if (z[i] == j) {
                return 0;
            }
        }

        int mov(int j, int i) {
            //move a value from one register to another
            z[i] = j;
        }
        int udiv(int j, int i) {
            return z[i] / j;
        }
        int sdiv(int j, int i) {
            return z[i] / j;
        }
        void lsl(int i) {
            z[i] = z[i] << 1;
        }
        void lsr(int i) {
            z[i] = z[i] >> 1;
        }
        void asr(int i) {
            z[i] = z[i] >> 1;
        }
        void ror(int i) {
            z[i] = z[i] >> 1;
        }
        int cbz(int i) {
            if (z[i] == 0) {
                return y[i];
            }
        }
        int cbnz(int i) {
            if (z[i] != 0) {
                return y[i];
            }
        }
        int cbeq(int i) {
            if (z[i] == 0) {
                return y[i];
            }
        }
        int cbne(int i) {
            if (z[i] != 0) {
                return y[i];
            }
        }
        int cble(int i) {
            if (z[i] <= 0) {
                return y[i];
            }
        }
        int cbgt(int i) {
            if (z[i] > 0) {
                return y[i];
            }
        }
        int ldm(int i) {
            return y[i];
        }
        int stm(int i) {
            return y[i];
        }
        float fadd(int j, int i) {
         return i+j;   
        }
        float fsub(int j, int i) {
            return i-j;
        }
        float fmul(int j, int i) {
            return i*j;
        }
        float fdiv(int j, int i) {
            return i/j;
        }
        float fmod(int j, int i) {
            return i%j;
        }
        int fcmp(int j, int i) {
            if (i == j) {
                return 0;
            } else {
                return 1;
            }
        }
        //ccmn instruction
        int ccmn(int j, int i) {
            if (i != j) {
                return 0;
            } else {
                return 1;
            }
        }
        //ccmp instruction
        int ccmp(int j, int i) {
            if (i == j) {
                return 0;
            } else {
                return 1;
            }
        }
        //csel instruction
        int csel(int j, int i) {
            if (i == j) {
                return 0;
            } else {
                return 1;
            }
        }
        //csinc instruction
        int csinc(int j, int i) {
            if (i == j) {
                return 0;
            } else {
                return 1;
            }
        }
        //csinv instruction
        int csinv(int j, int i) {
            if (i == j) {
                return 0;
            } else {
                return 1;
            }
        }
        //cneg instruction
        int cneg(int j, int i) {
            if (i == j) {
                return 0;
            } else {
                return 1;
            }
        }
        //sys instruction
        int sys(int i) {
            return 0;
        }
        //halt instructin
        int halt() {
            std::exit(1);
        }
        //HINT instruction
        int hint() {
            return 0;
        }
        //MSR instruction
        int msr() {
            return 0;
        }
        //MRS instruction
        int mrs() {
            return 0;
        }
        //BRK instruction
        int brk() {
            std::exit(0);
        }
        void umod(int j, int i) {
            z[i] %= j;
        }
        template <typename T>
        T ldr(const std::vector<unsigned char>& memory, uintptr_t address) {
            T value;
            std::memcpy(&value, memory.data() + address, sizeof(T));
            return value;
        }
        template <typename T>
        void str(std::vector<unsigned char>& memory, uintptr_t address, T value) {
            std::memcpy(memory.data() + address, &value, sizeof(T));
        }
    } instructionFunctions;
    static bool isTokenInArray(const std::vector<std::string>& array, const std::string& token) {
        return std::find(array.begin(), array.end(), token) != array.end();
    }
    static void executeInstruction(const std::string& instruction, const std::vector<std::string>& operands) {
        if (instruction == "add") {
            if (operands.size() == 2) {
                instructionFunctions.add(std::stoi(operands[0]), std::stoi(operands[1]));
            }
        } else if ( instruction == "sub") {
            if (operands.size() == 2) {
                instructionFunctions.sub(std::stoi(operands[0]), std::stoi(operands[1]));
            }
        } else if (instruction == "mul") {
            if (operands.size() == 2) {
                instructionFunctions.mul(std::stoi(operands[0]), std::stoi(operands[1]));
            }
        } else if (instruction == "div") {
            if (operands.size() == 2) {
                instructionFunctions.div(std::stoi(operands[0]), std::stoi(operands[1]));
            }
        } else if (instruction == "mod") {
            if (operands.size() == 2) {
                instructionFunctions.mod(std::stoi(operands[0]), std::stoi(operands[1]));
            }
        } else if (instruction == "cmp") {
            if (operands.size() == 2) {
                instructionFunctions.cmp(std::stoi(operands[0]), std::stoi(operands[1]));
            }
        } else if (instruction == "ccmn") {
            if (operands.size() == 2) {
                instructionFunctions.ccmn(std::stoi(operands[0]), std::stoi(operands[1]));
            }   
        } else if (instruction == "ccmp") {
            if (operands.size() == 2) {
                instructionFunctions.ccmp(std::stoi(operands[0]), std::stoi(operands[1]));
            }
        } else if (instruction == "csel") {
            if (operands.size() == 2) {
                instructionFunctions.csel(std::stoi(operands[0]), std::stoi(operands[1]));
            }
        } else if (instruction == "csinc") {
            if (operands.size() == 2) {
                instructionFunctions.csinc(std::stoi(operands[0]), std::stoi(operands[1]));
            }
        } else if (instruction == "csinv") {
            if (operands.size() == 2) {
                instructionFunctions.csinv(std::stoi(operands[0]), std::stoi(operands[1]));
            }
        } else if (instruction == "cneg") {
            if (operands.size() == 2) {
                instructionFunctions.cneg(std::stoi(operands[0]), std::stoi(operands[1]));
            }
        } else if (instruction == "sys") {
            instructionFunctions.sys(std::stoi(operands[0]));
        } else if (instruction == "halt") {
            instructionFunctions.halt();
        } else if (instruction == "hint") {
            instructionFunctions.hint();
        } else if (instruction == "msr") {
            instructionFunctions.msr();
        } else if (instruction == "mrs") {
            instructionFunctions.mrs();
        } else if (instruction == "brk") {
            instructionFunctions.brk();
        } else if (instruction == "lsl") {
            instructionFunctions.lsl(std::stoi(operands[0]));
        } else if (instruction == "lsr") {
            instructionFunctions.lsr(std::stoi(operands[0]));
        } else if (instruction == "asr") {
            instructionFunctions.asr(std::stoi(operands[0]));
        } else if (instruction == "ror") {
            instructionFunctions.ror(std::stoi(operands[0]));
        } else if (instruction == "cbz") {
            instructionFunctions.cbz(std::stoi(operands[0]));
        } else if (instruction == "cbnz") {
            instructionFunctions.cbnz(std::stoi(operands[0]));
        } else if (instruction == "cbeq") {
            instructionFunctions.cbeq(std::stoi(operands[0]));
        } else if (instruction == "cbne") {
            instructionFunctions.cbne(std::stoi(operands[0]));
        } else if (instruction == "cble") {
            instructionFunctions.cble(std::stoi(operands[0]));
        } else if (instruction == "cbgt") {
            instructionFunctions.cbgt(std::stoi(operands[0]));
        } else if (instruction == "ldr") {
            std::string intValue = operands[0];
            uintptr_t uintptrValue = std::stoull(intValue);
            instructionFunctions.ldr<int>(Memory, uintptrValue);
        } else if (instruction == "str") {
            std::string intValue = operands[0];
            uintptr_t uintptrValue = std::stoull(intValue);
            instructionFunctions.str(Memory, uintptrValue, operands[1]); //note: operands[1] is the value to be stored. it should be a string, for compatibility and future use.
        } else if (instruction == "f") {
            instructionFunctions.f(std::stoi(operands[0]), std::stoi(operands[1]));
        } else if (instruction == "mod") {
            instructionFunctions.mod(std::stoi(operands[0]), std::stoi(operands[1]));
        } else if (instruction == "extrh") {
            instructionFunctions.extrh(std::stoi(operands[0]), std::stoi(operands[1]));
        } else if (instruction == "extrx") {
            instructionFunctions.extrx(std::stoi(operands[0]));
        } else if (instruction == "extry") {
            instructionFunctions.extry(std::stoi(operands[0]));
        } else if (instruction == "b") {
            instructionFunctions.b(std::stoi(operands[0]));
        } else if (instruction == "beq") {
            instructionFunctions.beq(std::stoi(operands[0]));
        } else if (instruction == "bne") {
            instructionFunctions.bne(std::stoi(operands[0]));
        } else if (instruction == "orr") {
            instructionFunctions.orr(std::stoi(operands[0]), std::stoi(operands[1]));
        } else if (instruction == "eor") {
            instructionFunctions.eor(std::stoi(operands[0]), std::stoi(operands[1]));
        } else if (instruction == "bl") {
            instructionFunctions.bl(std::stoi(operands[0]));
        } else if (instruction == "mov") {
            instructionFunctions.mov(std::stoi(operands[0]), std::stoi(operands[1]));
        } else if (instruction == "udiv") {
            instructionFunctions.udiv(std::stoi(operands[0]), std::stoi(operands[1]));
        } else if (instruction == "sdiv") {
            instructionFunctions.sdiv(std::stoi(operands[0]), std::stoi(operands[1]));
        } else if (instruction == "umod") {
            instructionFunctions.umod(std::stoi(operands[0]), std::stoi(operands[1]));
        } else if (instruction == "smod") {
            instructionFunctions.umod(std::stoi(operands[0]), std::stoi(operands[1]));
        } else if (instruction == "and") {
            instructionFunctions.andInstuction(std::stoi(operands[0]), std::stoi(operands[1]));
        } else {
            std::cout << "Invalid instruction"  << std::endl;
            std::exit(1);
        }
        std::cout << "Successfully simulated instruction: " << instruction << std::endl;
    }
    //assembly function
     static void executeASM(std::string inputASM) {
        std::vector<std::string> operands;  // To store operands for each instruction
        //an array of all the names of the instruction functions, to be used later
        std::vector<std::string> instructionFunctionsNames = {"add", "sub", "mul", "div", "mod", "cmp", "ccmn", "ccmp", "csel", "csinc", "csinv", "cneg", "sys", "halt", "hint", "msr", "mrs", "brk", "lsl", "lsr", "asr", "ror", "cbz", "cbnz", "cbeq", "cbne", "cble", "cbgt", "ldr", "str", "f", "mod", "extrh", "extrx", "extry", "b", "beq", "bne", "orr", "eor", "bl", "mov", "udiv", "umod", "and"};
        std::string currentInstruction;     // To keep track of the current instruction
        virtual_machine vm;

        // Define a list of delimiters
        std::string delimiters = " ,;\n";


        std::vector<std::string> tokens = splitString(inputASM, delimiters);
        for (const std::string& token : tokens) {

        // if the instruction is and execute the andInstruction function
        if (token == "and") {
            instructionFunctions.andInstuction(std::stoi(operands[0]), std::stoi(operands[1]));
            return;
        }

        if (isTokenInArray(instructionFunctionsNames, token)) {
            if (!currentInstruction.empty()) {
                // Execute the previous instruction
                executeInstruction(currentInstruction, operands);
            }
            currentInstruction = token;
            operands.clear();
        } else {
            // Collect operands
            operands.push_back(token);
        }
         std::cout << "Simulation instruction added for processing." << std::endl;
    }

    // Execute the last instruction
    if (!currentInstruction.empty()) {
        executeInstruction(currentInstruction, operands);
    }
    std::cout << "Simulation instruction completed." << std::endl;
}
     

int main(){
    // get assembly code from user input
    std::string assembly;
    std::cout << "Enter assembly code: ";
    std::getline(std::cin, assembly);
    executeASM(assembly);
    return 0;
}
