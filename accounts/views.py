from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignupForm, ProfileForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido.')
            return redirect('blog:home')
        messages.error(request, 'Credenciales inválidas.')
    return render(request, 'accounts/login.html')

def signup(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, 'Registro exitoso.')
        return redirect('blog:home')
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def profile_edit(request):
    form = ProfileForm(request.POST or None, request.FILES or None, instance=getattr(request.user, 'profile', None))
    if request.method == 'POST' and form.is_valid():
        form.instance.user = request.user
        form.save()
        messages.success(request, 'Perfil actualizado.')
        return redirect('accounts:profile')
    return render(request, 'accounts/profile_edit.html', {'form': form})
