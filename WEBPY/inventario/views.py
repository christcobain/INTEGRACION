from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import  messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroForm

def home_view(request):
    # Verifica si el usuario está autenticado antes de mostrar la página de inicio
    if request.user.is_authenticated:
        # Muestra la página de inicio
        return render(request, 'about.html')
    else:
        # Redirige al usuario al formulario de login
        return redirect('login')
 
def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Maneja el caso de credenciales inválidas
            pass
    return render(request, 'users/login.html')   


def logout_view(request):
    logout(request)
    return redirect('login')

def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')