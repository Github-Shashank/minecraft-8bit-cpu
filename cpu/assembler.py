def assemble(code):

    lines = code.splitlines()

    output = []

    address = 0

    for line in lines:

        line = line.strip()

        if not line:
            continue

        binary = "00000000"

        # VERY TEMPORARY TEST

        if "ADD" in line:
            binary = "10000000"

        elif "SUB" in line:
            binary = "10000001"

        elif "JMP" in line:
            binary = "00100000"

        elif "CALL" in line:
            binary = "00101000"

        output.append(
            f"{address:04d} : {binary}"
        )

        address += 1

    return output