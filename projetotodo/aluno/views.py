from django.shortcuts import render
from django.http import HttpResponse

def minha_view(request):
    return HttpResponse("Realizado com sucesso a atividade")
