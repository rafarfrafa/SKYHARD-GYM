from django.urls import path

from . import views

urlpatterns = [
    path(
        '',
        views.home,
        name='home'),
    path(
        'sobre/',
        views.sobre,
        name='sobre'),
    path(
        'inscricao/',
        views.inscricao,
        name='inscricao'),
    path(
        'login/',
        views.login_view,
        name='login'),
    path(
        'Plano/',
        views.Plano,
        name='Plano'),
    path(
        'Treinadores/',
        views.Treinadores,
        name='Treinadores'),
    path(
        'Treinadores/<int:trainer_id>/',
        views.detalhes_treinador,
        name='detalhes_treinador'),
    path(
        'aulas/<int:class_id>/',
        views.detalhes_aula,
        name='detalhes_aula'),
    path(
        'Treinadores_detalhes/<int:trainer_id>/',
        views.Treinadores_detalhes,
        name='Treinadores_detalhes'),
]
