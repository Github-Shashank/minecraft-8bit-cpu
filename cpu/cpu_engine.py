# ==========================================
# CPU STATE
# ==========================================

cpu = {

    "PC": 0,

    "CENTER": "00000000",

    "W": "00000000",

    "CMP": False,

    "JUMP_REGISTER": "00000000",

    "R1R": "00000000",

    "R1L": "00000000",
}


# ==========================================
# RESET CPU
# ==========================================

def reset_cpu():

    cpu["PC"] = 0

    cpu["CENTER"] = "00000000"

    cpu["W"] = "00000000"

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
        # MEM VALUE
        # ==================================

        if tokens[0] == "MEM":

            if tokens[1] == "VALUE":

                value = tokens[2]

                cpu["CENTER"] = value

        # ==================================
        # INS
        # ==================================

        elif tokens[0] == "INS":

            # ------------------------------
            # W
            # ------------------------------

            if tokens[1] == "W":

                cpu["W"] = cpu["CENTER"]

            # ------------------------------
            # LD
            # ------------------------------

            elif tokens[1] == "LD":

                cpu["JUMP_REGISTER"] = cpu["CENTER"]

            # ------------------------------
            # JMP
            # ------------------------------

            elif tokens[1] == "JMP":

                if tokens[2] == "ONLY":

                    cpu["PC"] = int(
                        cpu["JUMP_REGISTER"],
                        2
                    )

            # ------------------------------
            # RET
            # ------------------------------

            elif tokens[1] == "RET":

                pass

        # ==================================
        # PC INCREMENT
        # ==================================

        cpu["PC"] += 1

    return cpu