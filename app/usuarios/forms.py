from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        # Aquí puedes realizar validaciones personalizadas si es necesario
        return cleaned_data


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'ci',)  # Agrega los campos necesarios para el registro de usuario

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['ci'].required = True  # Hace que el campo "ci" sea obligatorio en el formulario