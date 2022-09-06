from cleaning_functions import *
# for assembler

def create_dest():
    DEST = {
        "null": "000",
        "M": "001",
        "D": "010",
        "MD": "011",
        "A": "100",
        "AM": "101",
        "AD": "110"
    }
    return DEST

def create_comp():
    COMP = {
        "0": "0101010",
        "1": "0111111",
       "-1": "0111010",
        "D": "0001100",
        "A": "0110000", "M": "1110000",
       "!D": "0001101",
       "!A": "0110001", "!M": "1110001",
       "-D": "0001111",
       "-A": "0110011", "-M": "1110011",
      "D+1": "0011111",
      "A+1": "0110111", "M+1": "1110111",
      "D-1": "0001110",
      "A-1": "0110010", "M-1": "1110010",
      "D+A": "0000010", "A+D": "0000010", "D+M": "1000010", "M+D": "1000010",
      "D-A": "0010011", "D-M": "1010011",
      "A-D": "0000111", "M-D": "1000111",
      "D&A": "0000000", "A&D": "0000000", "D&M": "1000000", "M&D": "1000000",
      "D|A": "0010101", "A|D": "0010101", "D|M": "1010101", "M|D": "1010101"
    }
    return COMP

def create_jump():
    JUMP = {
        "null": "000",
        "JGT": "001",
        "JEQ": "010",
        "JGE": "011",
        "JLT": "100",
        "JNE": "101",
        "JLE": "110",
        "JMP": "111"
    }
    return JUMP

def create_symbol_table(filename):
    symbol_table = {
        "SP": 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4,
        "R0": 0,
        "R1": 1,
        "R2": 2,
        "R3": 3,
        "R4": 4,
        "R5": 5,
        "R6": 6,
        "R7": 7,
        "R8": 8,
        "R9": 9,
        "R10": 10,
        "R11": 11,
        "R12": 12,
        "R13": 13,
        "R14": 14,
        "R15": 15,
        "SCREEN": 16384,
        "KBD": 24576
    }
    with open(filename, "r") as file:
        pc = 0
        for line in file:
            line = line.strip("\n")
            line = clean(line)
            if not is_empty_or_comment(line):
                if is_label(line):
                    label = remove_parenthesis(line)

                    if label not in symbol_table:
                        symbol_table[label] = pc

                if is_instruction(line):
                    pc += 1

    with open(filename, "r") as file:
        next_address = 16
        for line in file:
            line = line.strip("\n")
            line = clean(line)
            if not is_empty_or_comment(line):
                if is_a_instruction(line):
                    a_instruction_val = line.strip("@")
                    if not a_instruction_val.isnumeric() and a_instruction_val not in symbol_table:
                        symbol_table[a_instruction_val] = next_address
                        next_address += 1
    return symbol_table

