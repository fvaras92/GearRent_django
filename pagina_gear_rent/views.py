from django.shortcuts import render
from .models import Product
# Create your views here.


def product_list(request):
    tipo_prod = request.GET.get('tipoprod')
    if tipo_prod:
        products = Product.objects.filter(tipoprod=tipo_prod)
    else:
        products = Product.objects.all

    return render(request, 'tienda/product_list.html', {'products': products})


