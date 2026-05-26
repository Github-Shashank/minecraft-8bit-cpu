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

    "RET": "00110000",

}


# =====================================
# ASSEMBLER
# =====================================

def assemble(code):

    lines = code.splitlines()

    output = []

    address = 0

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # Split instruction
        tokens = line.split()

        # Example:
        # DM ALU ADD
        #
        # tokens becomes:
        # ['DM', 'ALU', 'ADD']

        if tokens[0] == "DM":

            if tokens[1] == "ALU":

                operation = tokens[2]

                binary = ALU_OPS[operation]

                output.append(
                    f"{address:04d} : {binary}"
                )

                address += 1

            elif tokens[1] == "CMP":

                operation = tokens[2]

                binary = CMP_OPS[operation]

                output.append(
                    f"{address:04d} : {binary}"
                )

                address += 1

        elif tokens[0] == "INS":

            if tokens[1] == "RET":

                binary = INS_OPS["RET"]

                output.append(
                    f"{address:04d} : {binary}"
                )

                address += 1

    return output