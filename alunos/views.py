from django.shortcuts import render
from .models import Aluno

def cadastrar(request):
    aluno_cadastrado = None
    if request.method == 'POST':
        aluno_cadastrado = Aluno.objects.create(
            nome=request.POST.get('nome'),
            idade=request.POST.get('idade'),
            email=request.POST.get('email'),
            telefone=request.POST.get('telefone'),
            endereco=request.POST.get('endereco'),
            matricula=request.POST.get('matricula'),
            cpf=request.POST.get('cpf')
        )
    return render(request, 'alunos/cadastrar.html', {'aluno': aluno_cadastrado})

def listar(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/listar.html', {'alunos': alunos})