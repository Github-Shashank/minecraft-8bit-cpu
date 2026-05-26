from django.shortcuts import render

from .assembler import assemble


def index(request):

    assembly_code = ""

    binary_output = []

    if request.method == "POST":

        assembly_code = request.POST.get("code")

        binary_output = assemble(
            assembly_code
        )

    context = {

        "assembly_code": assembly_code,

        "binary_output": binary_output,
    }

    return render(
        request,
        "index.html",
        context
    )