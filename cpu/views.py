from django.shortcuts import render

def index(request):

    context = {

        "assembly_code": """
INS W
MEM VALUE 00010010

INS LD

INS JMP ONLY 00010010

DM ALU ADD

DM ARG R1R R2L

DM CMP =
""",

        "binary_output": [
            "0000 : 00111000",
            "0001 : 00010010",
            "0010 : 00110100",
            "0011 : 00100000",
        ]
    }

    return render(
        request,
        "index.html",
        context
    )