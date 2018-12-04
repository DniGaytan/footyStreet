from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout, authenticate, login
from django.urls import reverse
from .forms import UserForm

def register(request):
    form = UserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            login(request, user)

            return #Pagina de inicio
        else:
            if len(form.cleaned_data['password']) < 8:
                form.add_error('password', 'La contraseña es muy corta')
            if 'username' in form.errors:
                form.add_error('username', 'Una cuenta ya ha sido registrada con ese usuario')
            if 'email' in form.errors:
                form.add_error('email', 'Ingresa un correo valido')

            context = {
                'form': form,
                'errors': form.errors,
            }

            return render(request, template_name="User/register.html", context = context)#El signup form tiene errores
    else:
        if not request.user.is_authenticated:
            context = {
                'form': form,
                'errors': None,
            }

            return render(request, template_name="User/register.html", context = context)#El signup form se abre por primera vez
        else:
            return #Pagina de inicio

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return #Pagina principal
        else:
            context = {
                'form': UserForm(None),
                'errors': True
            }
            return render(request, template_name="User/login.html", context = context)#Login form tiene errores
    else:
        if not request.user.is_authenticated:
            context = {
                'form': UserForm(None),
                'error': False
            }
            return render(request, template_name="User/login.html", context = context)#Login por primera vez
        else:
            return #Pagina principal

def logout(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return #Pagina principal
        else:
            context = {
                'form': UserForm(None),
                'errors': True
            }
            return render(request, template_name="User/login.html", context = context)#Login form tiene errores
    else:
        if not request.user.is_authenticated:
            context = {
                'form': UserForm(None),
                'error': False
            }
            return render(request, template_name="User/login.html", context = context)#Login por primera vez
        else:
            return #Pagina principal
