from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def cartoes_parcelas(request):
    return render(request, "cartoes_parcelas.html")


def planejamento_mensal(request):
    return render(request, "planejamento_mensal.html")


def receitas_despesas(request):
    return render(request, "receitas_despesas.html")
