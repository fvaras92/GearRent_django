from django import forms
from .models import Registro
from .models import ContactForm

class RegistroForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Registro
        fields = ['nombre_completo', 'email', 'contraseña', 'rut']




class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'message']
