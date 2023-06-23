from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Registro
        fields = ['nombre_completo', 'email', 'contraseña', 'rut']
