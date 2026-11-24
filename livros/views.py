from django.shortcuts import render
from .models import Livro

def cadastrar(request):
    livro_cadastrado = None
    if request.method == 'POST':
        livro_cadastrado = Livro.objects.create(
            titulo=request.POST.get('titulo'),
            autor=request.POST.get('autor'),
            editora=request.POST.get('editora'),
            ano_publicacao=request.POST.get('ano_publicacao'),
            isbn=request.POST.get('isbn')
        )
    return render(request, 'livros/cadastrar.html', {'livro': livro_cadastrado})

def listar(request):
    livros = Livro.objects.all()
    return render(request, 'livros/listar.html', {'livros': livros})