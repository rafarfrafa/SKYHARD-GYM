from django.contrib import admin
from .models import Treinador, Plano, Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('user', 'telefone', 'Plano', 'nome_completo')


@admin.register(Treinador)
class TreinadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especialidade', 'email')
    search_fields = ('nome', 'email')
