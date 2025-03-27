from django.shortcuts import render

from .models import Class, Trainer, Plano


def home(request):
    trainers = Trainer.objects.all()
    classes = Class.objects.all()
    return render(request, 'site_academia/home.html',
                  {'trainers': trainers, 'classes': classes})


def detalhes_aula(request, class_id):
    class_info = Class.objects.get(id=class_id)
    return render(request,
                  'site_academia/detalhes_aula.html',
                  {'class': class_info})


def detalhes_treinador(request, trainer_id):

    trainer = Trainer.objects.get(id=trainer_id)
    return render(request,
                  'site_academia/detalhes_treinador.html',
                  {'trainer': trainer})


def inscricao(request):
    return render(request, 'site_academia/inscricao.html')


def login_view(request):
    return render(request, 'site_academia/login.html')


def lista_plano(request):
    Plano = Plano.objects.all()
    return render(request, 'site_academia/Plano.html', {'Plano': Plano})


def Treinadores_detalhes(request, trainer_id):

    trainer = Trainer.objects.get(id=trainer_id)
    return render(request,
                  'site_academia/Treinadores_detalhes.html',
                  {'trainer': trainer})


def Treinadores(request):
    trainers = Trainer.objects.all()
    return render(request,
                  'site_academia/Treinadores.html',
                  {'trainers': trainers})


def sobre(request):
    return render(request, 'site_academia/sobre.html')
