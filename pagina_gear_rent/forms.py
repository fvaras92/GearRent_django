from django import forms
from .models import Registro
from .models import ContactForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

#class RegistroForm(forms.ModelForm):
 #   contraseña = forms.CharField(widget=forms.PasswordInput)

  #  class Meta:
   #     model = Registro
    #    fields = ['nombre_completo', 'email', 'contraseña', 'rut']
class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Correo Electrónico")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    pass



class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'message']


class RegistroForm(UserCreationForm):
    class Meta:
        model = CustomUser
        
        print()