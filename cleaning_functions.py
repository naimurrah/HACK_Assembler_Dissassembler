import re

# functions that alter lines read for assembler
def to_15_bit(num):
    return "{0:015b}".format(num)

def is_empty_or_comment(line): # test
    if line == "" or line[0:2] == "//":
        return True
    return False

# test
def clean(line):
    clean_line = ""
    for letter in line:
        if letter == "/":
            break
        if letter != " ":
            clean_line += letter
    return clean_line


def is_a_instruction(line):
    if line[0] == "@":
        if line[1].isalpha() or line[1] == "_":
            for letter in line[2:]:
                if not (letter.isalnum() or letter == "_"):
                    return False
            return True
        elif line[1:].isnumeric():
            return True
    elif is_label(line):
        return True
    return False


def is_c_instruction(line, destTable, compTable, jumpTable): # test
    if not (line.count("=") == 1 or line.count(";") == 1) :
        return False

    tokens = re.split("[=;]", line)
    if len(tokens) != 2 and len(tokens) != 3:
        return False

    if len(tokens) == 2:
        if line.count("=") == 1:
            if not tokens[0] in destTable:
                return False
            if not tokens[1] in compTable:
                return False
        else:
            if not tokens[0] in compTable:
                return False
            if not tokens[1] in jumpTable:
                return False
    else:
        if not tokens[0] in destTable:
            return False
        if not tokens[1] in compTable:
            return False
        if not tokens[2] in jumpTable:
            return False
    return True

def is_label(line): # test
    if line[0] == "(" and line[len(line)-1] == ")" and is_valid_name(line[1:len(line)-1]):
        return True
    return False

def remove_parenthesis(line): # test
    return line[1:len(line)-1]

def is_instruction(line):
    if not is_empty_or_comment(line):
        return True
    return False

def is_valid_name(line):
    if line[0].isalpha() or line[0] == "_":
        for letter in line[1:]:
            if not (letter.isalnum() or letter == "_"):
                return False
        return True
    return False
