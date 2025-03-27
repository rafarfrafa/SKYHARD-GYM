from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Plano


@receiver(post_migrate)
def criar_planos_iniciais(sender, **kwargs):
    if sender.name == 'site_academia':  # Verifique se o signal é para o app correto
        planos = [
            {
                'nome': 'Plano Básico',
                'descricao': 'Acesso à academia em horários limitados.',
                'preco': 100.00,
                'data_inicio': '2023-10-01',
                'data_fim': '2023-12-31',
            },
            {
                'nome': 'Plano Intermediário',
                'descricao': 'Acesso à academia em horários estendidos.',
                'preco': 150.00,
                'data_inicio': '2023-10-01',
                'data_fim': '2023-12-31',
            },
            {
                'nome': 'Plano Avançado',
                'descricao': 'Acesso ilimitado à academia e aulas especiais.',
                'preco': 200.00,
                'data_inicio': '2023-10-01',
                'data_fim': '2023-12-31',
            },
        ]

        for plano in planos:
            Plano.objects.get_or_create(**plano)
