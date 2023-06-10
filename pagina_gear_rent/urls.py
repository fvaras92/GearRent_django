from django.urls import path
from . import views

urlpatterns = [
    path('tienda', views.product_list, name='product_list'),
]