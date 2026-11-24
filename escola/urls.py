from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('alunos.urls')),
    path('professor/', include('professor.urls')),
    path('livros/', include('livros.urls')),
]