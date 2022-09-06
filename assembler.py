import sys
import re
from symbol_tables import *
from cleaning_functions import *


def a_instruction(line, symbolTable):
    if not is_label(line):
        symbol = line[1:]
    else:
        symbol = remove_parenthesis(line)

    if symbol.isnumeric():
        bin = to_15_bit(int(symbol))
        return "0" + bin

    addr = symbolTable[symbol]
    bin = to_15_bit(addr)
    return "0" + bin

def c_instruction(line, destTable, compTable, jumpTable):
    tokens = re.split("[=;]", line)
    prefix = "111"
    dest = ""
    comp = ""
    jump = ""

    if len(tokens) == 2:
        if line.count("=") == 1:
            dest = destTable[tokens[0]]
            comp = compTable[tokens[1]]
            jump = "000"
            if dest == "" or comp == "":
                return "ERROR"
        else:
            dest = "000"
            comp = compTable[tokens[0]]
            jump = jumpTable[tokens[1]]

            if comp == "" or jump == "":
                return "ERROR"
    else:
        dest = destTable[tokens[0]]
        comp = compTable[tokens[1]]
        jump = jumpTable[tokens[2]]
        if comp == "" or jump == "" or dest == "":
            return "ERROR"

    return prefix + comp + dest + jump




def main():
    asmFileName = sys.argv[1]
    symbolTable = create_symbol_table(asmFileName)
    compTable = create_comp()
    destTable = create_dest()
    jumpTable = create_jump()

    binaryOut = asmFileName.split(".")[0] + ".hack"
    binaryFileOut = open(binaryOut, "w")

    with open(asmFileName, "r") as fin:
        for line in fin.readlines():
            line = line.strip("\n")
            line = clean(line)
            if is_empty_or_comment(line):
                continue

            if is_a_instruction(line):
                bin = a_instruction(line, symbolTable)
                binaryFileOut.write(bin + "\n")
                continue

            if is_c_instruction(line, destTable, compTable, jumpTable):
                bin = c_instruction(line, destTable, compTable, jumpTable)
                binaryFileOut.write(bin + "\n")
                continue

            return "ERROR"

    binaryFileOut.close()
    return "SUCCESS: " + binaryOut + " created"

print(main())