from django.shortcuts import render
from .models import *

# Create your views here.

def listaTarefas(request):
    html = "<h1>Lista de Tarefas</h1>"
    listaTarefa = Tarefa.objects.all()
    for evento in listaTarefa:
        html += '<li><strong>{}</strong></li>'.format(tarefa.nome)
    return HttpResponse(html)
