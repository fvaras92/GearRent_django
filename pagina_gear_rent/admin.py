from django.contrib import admin
from .models import Product,CustomUser
from django.contrib.auth.admin import UserAdmin
admin.site.register(Product)


class CustomUserAdmin(UserAdmin):
    # Personaliza los campos a mostrar en la vista de lista de usuarios
    list_display = ('username', 'email', 'rut', 'is_staff')

    # Personaliza los campos de búsqueda en la vista de lista de usuarios
    search_fields = ('username', 'email', 'rut')

    # Personaliza los filtros disponibles en la vista de lista de usuarios
    list_filter = ('is_staff', 'is_superuser', 'groups')

    # Personaliza el formulario de edición de usuario en el administrador
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Información Personalizada', {'fields': ('rut',)}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas Importantes', {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)

    