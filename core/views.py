from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")

@login_required
def simulacao_saude(request):
    if request.method == "POST":
        base = float(request.POST.get("base", 0))
        fus = float(request.POST.get("fus", 0))
        tesouro = float(request.POST.get("tesouro", 0))
        transf = float(request.POST.get("transf", 0))

        gasto_total = fus + tesouro + transf
        minimo = base * 0.15
        percentual = gasto_total / base * 100 if base > 0 else 0
        diferenca = gasto_total - minimo

        contexto = {
            "base": base,
            "fus": fus,
            "tesouro": tesouro,
            "transf": transf,
            "gasto_total": gasto_total,
            "minimo": minimo,
            "percentual": percentual,
            "diferenca": diferenca,
        }
        return render(request, "simulacao_saude.html", contexto)

    return render(request, "simulacao_saude.html")
