DATA_MEMORY = [

    "00000000"
    for _ in range(32)

]
# ==========================================
# CPU STATE
# ==========================================

cpu = {

    "PC": 0,

    "CENTER": "00000000",

    "CMP": False,

    "JUMP_REGISTER": "00000000",

    "R1R": "00000000",

    "R1L": "00000000",

    "DATA_MEMORY": DATA_MEMORY,
}


# ==========================================
# RESET CPU
# ==========================================

def reset_cpu():

    cpu["PC"] = 0

    cpu["CENTER"] = "00000000"

    cpu["CMP"] = False

    cpu["JUMP_REGISTER"] = "00000000"

    cpu["R1R"] = "00000000"

    cpu["R1L"] = "00000000"


# ==========================================
# EXECUTE PROGRAM
# ==========================================

def execute_program(lines):

    reset_cpu()

    for line in lines:

        line = line.strip()

        # Remove comments
        line = line.split(";")[0]

        if not line:
            continue

        tokens = line.split()

        # ==================================
        # MEM
        # ==================================

        if tokens[0] == "MEM":

            value = int(tokens[1])

            cpu["CENTER"] = format(
                value,
                "08b"
            )

        # ==================================
        # INS
        # ==================================

        elif tokens[0] == "INS":

            # ------------------------------
            # NOP
            # ------------------------------

            if tokens[1] == "NOP":

                pass

            # ------------------------------
            # HLT
            # ------------------------------

            elif tokens[1] == "HLT":

                break

            # ------------------------------
            # LD
            # ------------------------------

            elif tokens[1] == "LD":

                cpu["CENTER"] = format(
                    cpu["PC"],
                    "08b"
                )

            # ------------------------------
            # W
            # ------------------------------

            elif tokens[1] == "W":

                cpu["JUMP_REGISTER"] = (
                    cpu["CENTER"]
                )

            # ------------------------------
            # JMP
            # ------------------------------

            elif tokens[1] == "JMP":

                mode = tokens[2]

                # JMP ONLY

                if mode == "ONLY":

                    cpu["PC"] = int(
                        cpu["JUMP_REGISTER"],
                        2
                    )

                # JMP IF

                elif mode == "IF":

                    if cpu["CMP"]:

                        cpu["PC"] = int(
                            cpu["JUMP_REGISTER"],
                            2
                        )

                # JMP IF NOT

                elif mode == "IF_NOT":

                    if not cpu["CMP"]:

                        cpu["PC"] = int(
                            cpu["JUMP_REGISTER"],
                            2
                        )

            # ------------------------------
            # CALL
            # ------------------------------

            elif tokens[1] == "CALL":

                pass

            # ------------------------------
            # RET
            # ------------------------------

            elif tokens[1] == "RET":

                pass


        # ==================================
        # DATA
        # ==================================

        elif tokens[0] == "DATA":

            operation = tokens[1]

            address = int(tokens[2])

            # ------------------------------
            # DATA LD
            # ------------------------------

            if operation == "LD":

                cpu["CENTER"] = (
                    cpu["DATA_MEMORY"][address]
                )

        
            # ------------------------------
            # DATA W
            # ------------------------------

            elif operation == "W":

                cpu["DATA_MEMORY"][address] = (
                    cpu["CENTER"]
                )
            
        # ==================================
        # PC INCREMENT
        # ==================================

        cpu["PC"] += 1

    return cpu