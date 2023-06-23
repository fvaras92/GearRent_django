from django.shortcuts import render
from .models import Product
from django.shortcuts import redirect, get_object_or_404
from decimal import Decimal
from .forms import RegistroForm, ContactFormForm

# Create your views here.


def product_list(request):
    tipo_prod = request.GET.get('tipoprod')
    products = Product.objects.filter(tipoprod=tipo_prod)
   

    return render(request, 'tienda/product_list.html', {'products': products})

def mi_vista(request):
    return render(request, 'tienda/carrusel.html')

def index(request):
    return render(request, 'tienda/index.html')

def login(request):
    return render(request, 'login.html')

def carrusel_view(request):
    # Lógica de la vista...
    return render(request, 'carrusel.html')
def accesorios(request):
    # Lógica de la vista
    return render(request, 'accesorios.html')

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'tienda/login.html', {'form': form})

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

