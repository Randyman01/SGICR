from django import forms
from .models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'primer_apellido', 'segundo_apellido', 'carnet_identidad', 'usuario', 'password', 'confirmar_password', 'rol']
        # Otros campos que desees incluir
