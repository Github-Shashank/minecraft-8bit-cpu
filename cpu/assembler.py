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

                value = int(tokens[1])

                if value < 0 or value > 63:

                    raise Exception(
                        "MEM value must be 0-63"
                    )

                value_bits = format(
                    value,
                    "06b"
                )

                binary = "11" + value_bits

                output.append(
                    f"{address:04d} : {binary}"
                )

                address += 1

            # =====================================
            # DATA
            # =====================================

            elif tokens[0] == "DATA":

                operation = tokens[1]

                address_value = int(tokens[2])

                if address_value < 0 or address_value > 31:

                    raise Exception(
                        "DATA address must be 0-31"
                    )

                address_bits = format(
                    address_value,
                    "05b"
                )

                # DATA LD
                if operation == "LD":

                    binary = "010" + address_bits

                # DATA W
                elif operation == "W":

                    binary = "011" + address_bits

                else:

                    raise Exception(
                        "Unknown DATA operation"
                    )

                output.append(
                    f"{address:04d} : {binary}"
                )

                address += 1
            
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