from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1>Financial Control</h1><p>Sistema de controle financeiro pessoal</p>")
