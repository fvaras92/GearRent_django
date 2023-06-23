from django.shortcuts import render
from .models import Product
# Create your views here.


def product_list(request):
    tipo_prod = request.GET.get('tipoprod')
    products = Product.objects.filter(tipoprod=tipo_prod)
   

    return render(request, 'tienda/product_list.html', {'products': products})

def mi_vista(request):
    return render(request, 'tienda/carrusel.html')

def index(request):
    return render(request, 'tienda/index.html')

def carrusel_view(request):
    # Lógica de la vista...
    return render(request, 'carrusel.html')


