from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Cliente, Plano


class ClienteForm(UserCreationForm):
    nome_completo = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Nome completo'}),
        error_messages={
            'required': 'Por favor, insira seu nome completo.',
        }
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'seuemail@email.com'}),
        error_messages={
            'required': 'Por favor, insira um endereço de e-mail válido.',
        }
    )
    telefone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': '(11) 98765-4321'}),
        error_messages={
            'required': 'Por favor, insira um número de telefone válido.',
        }
    )
    Plano = forms.ModelChoiceField(
        queryset=Plano.objects.all(),
        empty_label="Selecione um plano",
        error_messages={
            'required': 'Por favor, selecione um plano.',
        }
    )

    class Meta:
        model = User
        fields = [
            'username',
            'nome_completo',
            'email',
            'telefone',
            'Plano',
            'password1',
            'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError(
                "Este nome de usuário já está em uso. Por favor, escolha outro.")
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["nome_completo"]
        user.email = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
            cliente = Cliente.objects.create(
                user=user,
                telefone=self.cleaned_data["telefone"],
                Plano=self.cleaned_data["Plano"],
                nome_completo=self.cleaned_data["nome_completo"]
            )
            return cliente
        return user
