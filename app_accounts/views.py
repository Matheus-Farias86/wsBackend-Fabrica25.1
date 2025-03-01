from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm, ChangePasswordForm, CustomUserCreationForm
from app_rick.models import Favorito


def cadastroView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST) # Cria um form com os dados do POST
        if form.is_valid(): # Salva o user e loga automaticamente
            user = form.save()
            login(request, user)
            return redirect('perfil')  # Redireciona para a página de perfil
    else:
        form = CustomUserCreationForm() # Formulário vazio

    return render(request, 'cadastro.html', {'form': form}) # Renderização do template


def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('perfil')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def perfilView(request):
    favoritos = Favorito.objects.filter(usuario=request.user) # Obtém favoritos do model Favorito do app_rick
    return render(request, 'perfil.html', {'user': request.user, 'favoritos': favoritos})

def editarView(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Seu perfil foi atualizado com sucesso!")
            return redirect('perfil')  # Redireciona para a página de perfil
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'edit_perfil.html', {'form': form})

def deletarView(request):
    user = request.user
    user.delete()
    return redirect('cadastro')

def logoutView(request):
    logout(request)
    return redirect('login')

@login_required
def alterarSenhaView(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) # Atualiza a sessão do user pra forçar o logout
            messages.success(request, "Senha alterada com sucesso!")
            return redirect('perfil')
        else:
            messages.error(request, "Corrija os erros abaixo.")
    else:
        form = ChangePasswordForm(request.user)

    return render(request, 'alterar_senha.html', {'form': form})