from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from .forms import ClienteForm
from .models import Cliente, Treinador, Plano
import logging

logger = logging.getLogger(__name__)


def home(request):
    return render(request, 'site_academia/home.html')


def sobre(request):
    return render(request, 'site_academia/sobre.html')


def plano(request):
    planos = Plano.objects.all()
    return render(request, 'site_academia/plano.html', {'planos': planos})


def contato(request):
    return render(request, 'site_academia/contato.html')


def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        print("Dados recebidos:", request.POST)  # Para debug
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('home')
        else:
            print("Erros no formulário:", form.errors)  # Para debug
            logger.error(f"Erros no formulário: {form.errors}")
            messages.error(request, "Por favor, corrija os erros abaixo.")
    else:
        form = ClienteForm()

    return render(request,
                  'site_academia/cadastrar_cliente.html',
                  {'form': form})


def treinadores(request):
    treinadores = Treinador.objects.all()
    return render(request,
                  'site_academia/treinadores.html',
                  {'treinadores': treinadores})


class CustomLoginView(LoginView):
    template_name = 'site_academia/login.html'
    redirect_authenticated_user = True  # Redireciona usuários já autenticados
    # Redireciona para a página de planos após o login
    success_url = reverse_lazy('plano')

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Usuário ou senha incorretos. Tente novamente.")
        return super().form_invalid(form)


def logout_usuario(request):
    logout(request)
    return redirect('home')
