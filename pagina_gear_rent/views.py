from django.shortcuts import render
from .models import Product
from django.shortcuts import redirect, get_object_or_404
from decimal import Decimal
from .forms import LoginForm, RegistroForm, ContactFormForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def product_list(request):
    tipo_prod = request.GET.get('tipoprod')
    products = Product.objects.filter(tipoprod=tipo_prod)
   

    return render(request, 'tienda/product_list.html', {'products': products})

def mi_vista(request):
    return render(request, 'tienda/carrusel.html')

def index(request):
    return render(request, 'tienda/index.html')

def login_view(request):
    form_type = 'login'
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('tienda')  # Redirigir a la página de la tienda
            else:
                form.add_error(None, "Credenciales inválidas. Verifica tu correo y contraseña.")
    else:
        form = LoginForm()
    return render(request, 'tienda/login.html', {'form': form, 'form_type': form_type})

def carrusel_view(request):
    # Lógica de la vista...
    return render(request, 'carrusel.html')
def accesorios(request):
    # Lógica de la vista
    return render(request, 'accesorios.html')

def registro_view(request):
    form_type = 'registro'
    print(request.POST)  # Depuración: Imprime los datos del formulario en la consola
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            print("El formulario es válido")            
            # Autenticación del usuario recién registrado
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                # Autenticación fallida, puedes manejar el caso aquí
                pass
            
            return redirect('login')
        else:
            print(form.errors)  # Depuración: Imprime los errores del formulario en la consola
    else:
        form = RegistroForm()
    return render(request, 'tienda/login.html', {'form': form, 'form_type': form_type})

def privacidad(request):
    return render(request, 'privacidad.html')
def soporte(request):
    return render(request, 'soporte.html')
def terminos(request):
    return render(request, 'terminos.html')

def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            # Aquí puedes enviar notificaciones por correo electrónico si deseas
            return redirect('contact_success')
    else:
        form = ContactFormForm()
    
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')

