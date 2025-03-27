from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('plano/', views.plano, name='plano'),
    path('contato/', views.contato, name='contato'),
    path('cadastro/', views.cadastrar_cliente, name='cadastro'),
    path('treinadores/', views.treinadores, name='treinadores'),
    path(
        'login/',
        views.CustomLoginView.as_view(),
        name='login'),
    # Página de login
    path('logout/', views.logout_usuario, name='logout'),
]
