from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name='listar_alunos'),
    path('listar/', views.listar, name='listar_alunos'),
    path('cadastrar/', views.cadastrar, name='cadastrar_alunos'),     
]