from django.shortcuts import render
from .cpu_engine import execute_program
from .assembler import assemble


def index(request):

    assembly_code = ""

    binary_output = []

    cpu_state = {}

    if request.method == "POST":

        assembly_code = request.POST.get("code")

        binary_output = assemble(
            assembly_code
        )

        cpu_state = execute_program(
            assembly_code.splitlines()
        )

    context = {

        "assembly_code": assembly_code,

        "binary_output": binary_output,

        "cpu_state": cpu_state,
    }

    return render(
        request,
        "index.html",
        context
    )