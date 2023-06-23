from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('tienda', views.product_list, name='product_list'),
    path('tienda', views.mi_vista, name='carrusel'),
    path('tienda', views.mi_vista, name='index'),
    path('pagina_gear_rent/templates/login/', views.login, name='login'),
    path('pagina_gear_rent/index', views.index, name='index'),
    path('carrusel/', views.carrusel_view, name='carrusel'),
    path('pagina_gear_rent/templates/accesorios/', views.accesorios, name='accesorios'),
    path('login', views.registro_view, name='login'),
    path('pagina_gear_rent/templates/privacidad/', views.privacidad, name='privacidad'),
    path('pagina_gear_rent/templates/soporte/', views.soporte, name='soporte'),
    path('pagina_gear_rent/templates/terminos/', views.terminos, name='terminos'),
    #path('carro', views.Carro, name='carro'),
    #path('agregar_producto/<int:product_id>/', views.agregar_producto, name='agregar_producto'),

    #path('pagina_gear_rent/', views.mi_vista, name='index'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)