from django.shortcuts import render
from .models import Professor

def cadastrar(request):
    prof_cadastrado = None
    if request.method == 'POST':
        prof_cadastrado = Professor.objects.create(
            nome=request.POST.get('nome'),
            disciplina=request.POST.get('disciplina'),
            email=request.POST.get('email'),
            telefone=request.POST.get('telefone')
        )
    return render(request, 'professor/cadastrar.html', {'professor': prof_cadastrado})

def listar(request):
    professores = Professor.objects.all()
    return render(request, 'professor/listar.html', {'professores': professores})