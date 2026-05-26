from .cpu_engine import execute_program

# =====================================
# OPCODE TABLES
# =====================================

ALU_OPS = {

    "ADD": "10000000",
    "SUB": "10000001",

}

CMP_OPS = {

    "=": "11100000",

}

INS_OPS = {

    "NOP": "00000000",
    "HLT": "00000001",

    "JMP_ONLY": "00001000",
    "JMP_IF": "00001010",
    "JMP_IF_NOT": "00001011",

    "CALL": "00001100",
    "RET": "00001101",

    "LD": "00001110",
    "W": "00001111",
}

# =====================================
# ASSEMBLER
# =====================================

def assemble(code):

    lines = code.splitlines()

    output = []

    address = 0

    for line_number, line in enumerate(lines, start=1):

        original_line = line

        line = line.strip()

        # Remove comments
        line = line.split(";")[0]

        if not line:
            continue

        try:

            tokens = line.split()

            # =====================================
            # MEM
            # =====================================

            if tokens[0] == "MEM":

                if tokens[1] == "VALUE":

                    value = tokens[2]

                    output.append(
                        f"{address:04d} : {value}"
                    )

                    address += 1

                else:

                    raise Exception(
                        "Unknown MEM instruction"
                    )

            # =====================================
            # INS
            # =====================================

            elif tokens[0] == "INS":

                if tokens[1] == "NOP":

                    binary = INS_OPS["NOP"]

                elif tokens[1] == "HLT":

                    binary = INS_OPS["HLT"]

                elif tokens[1] == "JMP":

                    if tokens[2] == "ONLY":

                        binary = INS_OPS["JMP_ONLY"]

                    elif tokens[2] == "IF":

                        binary = INS_OPS["JMP_IF"]

                    elif tokens[2] == "IF_NOT":

                        binary = INS_OPS["JMP_IF_NOT"]

                    else:

                        raise Exception(
                            "Invalid JMP mode"
                        )

                elif tokens[1] == "CALL":

                    binary = INS_OPS["CALL"]

                elif tokens[1] == "RET":

                    binary = INS_OPS["RET"]

                elif tokens[1] == "LD":

                    binary = INS_OPS["LD"]

                elif tokens[1] == "W":

                    binary = INS_OPS["W"]

                else:

                    raise Exception(
                        "Unknown INS instruction"
                    )

                output.append(
                    f"{address:04d} : {binary}"
                )

                address += 1

            else:

                raise Exception(
                    "Unknown instruction type"
                )

        except Exception as e:

            output.append(
                f"ERROR LINE {line_number} : {str(e)}"
            )
    return output   