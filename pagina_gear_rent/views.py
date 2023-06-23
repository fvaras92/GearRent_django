from django.shortcuts import render
from .models import Product
from django.shortcuts import redirect, get_object_or_404
from decimal import Decimal
from .forms import RegistroForm

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

