import sys
DEST = {
        "000": "null",
        "001": "M",
        "010": "D",
        "011": "MD",
        "100": "A",
        "101": "AM",
        "110": "AD"
    }

JUMP = {
        "000": "null",
        "001": "JGT",
        "010": "JEQ",
        "011": "JGE",
        "100": "JLT",
        "101": "JNE",
        "110": "JLE",
        "111": "JMP"
    }

COMP = {
        "0101010": "0",
        "0111111": "1",
        "0111010":"-1",
        "0001100": "D",
        "0110000": "A", "1110000": "M",
        "0001101": "!D",
        "0110001": "!A", "1110001": "!M",
        "0001111": "-D",
        "0110011": "-A", "1110011": "-M",
        "0011111": "D+1",
        "0110111": "A+1", "1110111": "M+1",
        "0001110": "D-1",
        "0110010": "A-1", "1110010": "M-1",
        "0000010": "D+A", "1000010": "D+M",
        "0010011": "D-A", "1010011": "D-M",
        "0000111": "A-D", "1000111": "M-D",
        "0000000": "D&A", "1000000": "D&M",
        "0010101": "D|A", "1010101": "D|M"
    }

def clean(line):
    new_str = ""
    for letter in line:
        if letter == "0" or letter == "1":
            new_str += letter
        else:
            break
    return new_str

def is_binary(num_string):
    if num_string == "" or len(num_string) != 16:
        return False
    for letter in num_string:
        if not (letter == "1" or letter == "0"):
            return False
    return True

def main():
    hack_file_name = sys.argv[1]
    asm_file_name = hack_file_name.split(".")[0] + ".asm"
    asmFile = open(asm_file_name, "w")
    with open(hack_file_name, "r") as hackFile:
        for line in hackFile.readlines():
            line = line.strip("\n")
            line = clean(line)
            if is_binary(line):
                # a instruction
                if line[0] == "0":
                    a_number = int(line[1:], 2)
                    asmFile.write("@{:}\n".format(a_number))
                # c instruction
                elif line[0:3] == "111":
                    dest = DEST[line[10:13]]
                    comp = COMP[line[3:10]]
                    jump = JUMP[line[13:]]
                    # dest=comp;jump
                    if dest == "null":
                        asmFile.write(comp + ";" + jump + "\n")
                    elif jump == "null":
                        asmFile.write(dest + "=" + comp + "\n")
                    else:
                        asmFile.write(dest + "=" + comp + ";" + jump + "\n")
                else:
                    return "ERROR"
            else:
                continue
    asmFile.close()
    return "SUCCESS: " + asm_file_name + " created"


#print(main())

print("line: ", clean("10001// palin.asm adsfjhkasdfhasdf"))