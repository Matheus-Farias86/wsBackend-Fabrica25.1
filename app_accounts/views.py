from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm, ChangePasswordForm

def cadastroView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'cadastro.html', {'form': form})

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
    return render(request, 'perfil.html', {'user': request.user})

def editarView(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email', user.email)
        user.save()
        return redirect('perfil')
    return render(request, 'edit_perfil.html', {'user': request.user})

def deletarView(request):
    user = request.user
    user.delete()
    return redirect('cadastro')

def logoutView(request):
    logout(request)
    return redirect('login')

@login_required
def editView(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'edit_perfil.html', {'form': form})

@login_required
def alterarSenhaView(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Senha alterada com sucesso!")
            return redirect('perfil')
        else:
            messages.error(request, "Corrija os erros abaixo.")
    else:
        form = ChangePasswordForm(request.user)

    return render(request, 'alterar_senha.html', {'form': form})