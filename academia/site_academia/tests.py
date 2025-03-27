from django.test import TestCase
from .models import Cliente, Treinador, Plano
from django.contrib.auth.models import User


class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.Plano = Plano.objects.create(
            nome='Plano Básico', descricao='Plano básico')
        self.cliente = Cliente.objects.create(
            user=self.user,
            telefone='123456789',
            Plano=self.Plano,
            email='test@example.com',
            nome_completo='Test User')
        self.treinador = Treinador.objects.create(
            nome='Treinador Teste',
            idade=30,
            especialidade='Musculação',
            email='treinador@example.com',
            telefone='987654321')

    def test_cliente_str(self):
        self.assertEqual(str(self.cliente), 'testuser')

    def test_treinador_str(self):
        self.assertEqual(str(self.treinador), 'Treinador Teste')

    def test_plano_str(self):
        self.assertEqual(str(self.Plano), 'Plano Básico')
