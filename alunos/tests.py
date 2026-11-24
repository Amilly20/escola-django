from django.test import TestCase
from django.urls import reverse

from .models import Aluno


class CadastroAlunoTests(TestCase):
    def test_formulario_envia_e_cadastra_aluno(self):
        response = self.client.get(reverse('cadastrar_alunos'))
        content = response.content.decode()
        self.assertRegex(
            content,
            r'<form method="POST">[\s\S]*name="nome"[\s\S]*name="cpf"'
            r'[\s\S]*<button type="submit">Cadastrar</button>[\s\S]*</form>',
        )

        response = self.client.post(
            reverse('cadastrar_alunos'),
            {
                'nome': 'Ana Silva',
                'idade': 16,
                'email': 'ana@example.com',
                'telefone': '11999999999',
                'endereco': 'Rua das Flores',
                'matricula': 'A123',
                'cpf': '12345678901',
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Aluno.objects.filter(nome='Ana Silva').exists())
        self.assertContains(response, 'Aluno cadastrado com sucesso!')

    def test_navegacao_exibe_links_em_todas_as_paginas(self):
        page_routes = (
            'cadastrar_alunos',
            'listar_alunos',
            'cadastrar_professor',
            'listar_professores',
            'cadastrar_livro',
            'listar_livros',
        )
        registration_routes = (
            'cadastrar_alunos',
            'cadastrar_professor',
            'cadastrar_livro',
        )

        for page_route in page_routes:
            response = self.client.get(reverse(page_route))
            self.assertEqual(response.status_code, 200)
            for registration_route in registration_routes:
                self.assertContains(response, reverse(registration_route))
