from django.db import models
from django.contrib.auth.models import User


class Plano(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15)
    # Campo corrigido para "Plano"
    Plano = models.ForeignKey(Plano, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Treinador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    especialidade = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    foto = models.ImageField(upload_to='treinadores/', null=True, blank=True)

    def __str__(self):
        return self.nome
