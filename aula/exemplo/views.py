from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from aula.exemplo.models import Person

# Create your views here.
def teste(request):
    return HttpResponse("Conteúdo do Site")


def saudacao(request):
    hoje = datetime.now()
    if hoje.hour <= 12:
        mensagem = "Bom dia"
    elif 12 <= hoje.hour <= 18:
        mensagem = "Boa tarde"
    else:
        mensagem = "Boa noite"

    contexto = {
        "valor": mensagem
    }
    return render(request, "exemplo/arquivo.html", contexto)


def parametro(request, nome):
    nome = nome.upper()
    return HttpResponse(nome)


def contar(request, nome):
    tamanho = len(nome)
    return HttpResponse(tamanho)


def index(request):
    return render(request, 'base.html',context={"valor": "Bruno"},)


def person(request,id):
    p1 = Person.objects.get(id=id)
    contexto = {
        "person": p1
    }
    return render(request, "exemplo/person.html", contexto)


def list_persons(request):
    p1 = Person.objects.all()
    contexto = {
        "persons": p1
    }
    return render(request, "exemplo/persons.html", contexto)


