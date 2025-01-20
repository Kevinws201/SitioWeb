from django.http import HttpResponse
from django.shortcuts import render,redirect,redirect
from django.contrib.auth import login, update_session_auth_hash
from .forms import CustomUserCreationForm,CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.urls import reverse_lazy
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def login_required_with_message(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, "Por favor, inicie sesión para acceder a esta página.")
            return redirect('login')  # Asegúrate de que 'login' es el nombre de tu vista de inicio de sesión
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def index(request):
    numero = 0
    return render(request, "index.html",{'numero': numero})

def about(request):
    return render(request,"about.html")

def Home(request):
    numero = 0
    return render(request,'index.html',{'numero':numero})

def Login(request):
    numero = 0
    return render(request,'login.html', {'numero':numero})


def Register(request):
    numero = 0
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})

@login_required_with_message
def mainMenu(request):
    numero = 1
    return render(request, 'mainMenu.html', {'numero':numero})

@login_required_with_message
def Estatus(request):
    numero = 1
    return render(request,'estatus.html', {'numero':numero})

def RestorePassword(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Mantiene al usuario autenticado
            messages.success(request,"Contraseña Restablecida exitosamente")
            return redirect("home")
        else:
            messages.error(request, 'Por favor corrige los errores indicados.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'restorePassword.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('mainMenu')  # Redirige al nombre de URL 'home' después de iniciar sesión

from django.core.mail import send_mail
def enviar_correo(request):
    asunto = 'Restablecimiento de contraseña'
    mensaje = 'Codigo: '
    remitente = 'l21212019@tectijuana.edu.mx'  # Mismo correo configurado en EMAIL_HOST_USER
    destinatarios = ['kevinsexy5000@gmail.com']  # Cambia esto por el correo de destino
    try:
        send_mail(asunto, mensaje, remitente, destinatarios)
        return HttpResponse('Correo enviado exitosamente.')
    except Exception as e:
        return HttpResponse(f'Error al enviar el correo: {str(e)}')
def SecurityPassword(request):
    numero = 0
    return render(request,'securityPassword.html', {'numero':numero})