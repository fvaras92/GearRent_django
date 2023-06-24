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
    return render(request, 'login.html', {'form': form, 'form_type': form_type})

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


from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Product

def carrito(request):
    productos = Product.objects.all()

    # Obtener los datos del carrito del usuario desde la sesión
    carrito = request.session.get('carrito', {})
    total = 0

    # Actualizar el total y el stock de cada producto en el carrito
    for producto_id, cantidad in carrito.items():
        producto = Product.objects.get(id=producto_id)
        producto.stock -= cantidad
        producto.save()
        total += producto.precio * cantidad

    # Guardar el total en la sesión
    request.session['total_carrito'] = total

    # Renderizar la página del carrito con los productos y el total
    context = {
        'productos': productos,
        'total': total,
    }
    return render(request, 'carrito.html', context)
from django.http import JsonResponse

def agregar_producto(request, producto_id):
    # Obtener los datos del carrito del usuario desde la sesión
    carrito = request.session.get('carrito', {})
    
    # Agregar el producto al carrito
    carrito[producto_id] = carrito.get(producto_id, 0) + 1
    
    # Guardar los datos actualizados del carrito en la sesión
    request.session['carrito'] = carrito
    
    # Devolver una respuesta JSON con los datos actualizados del carrito
    return JsonResponse({'carrito': carrito})

def eliminar_producto(request, producto_id):
    # Obtener los datos del carrito del usuario desde la sesión
    carrito = request.session.get('carrito', {})
    
    # Eliminar el producto del carrito si existe
    if producto_id in carrito:
        del carrito[producto_id]
    
    # Guardar los datos actualizados del carrito en la sesión
    request.session['carrito'] = carrito
    
    # Devolver una respuesta JSON con los datos actualizados del carrito
    return JsonResponse({'carrito': carrito})
