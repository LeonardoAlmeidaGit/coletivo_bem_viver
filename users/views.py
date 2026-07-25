from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm


def login_view(request):
    if request.user.is_authenticated:
        return _redirect_after_login(request.user)

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Bem-vindo(a), {user.username}')
            return _redirect_after_login(user)
        else:
            messages.error(request, 'Usuário ou senha inválidos')
    else:
        form = LoginForm(request)
    return render(request, 'login.html', {'form': form})


def _redirect_after_login(user):
    if user.is_superuser:
        return redirect('home')
    try:
        kitchen = user.kitchen
        return redirect('kitchen_update', pk=kitchen.pk)
    except Exception:
        return redirect('kitchen_create')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Você saiu com sucesso.')
    return redirect('home')


def cadastro_view(request):
    return render(request, 'cadastro.html')
