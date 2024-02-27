from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.views import View
from django.contrib.auth import authenticate, login, get_user_model, update_session_auth_hash, logout
from .forms import UserLoginForm, CustomUserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CustomUser
from django.views.generic import ListView
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User


class LoginView(View):
    template_name = 'registration/pages-login.html'
    form_class = UserLoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirigir a una página de éxito o a la página principal
                return redirect('index')

        return render(request, self.template_name, {'form': form})


class RegisterUserView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'administration/crear_usuario.html'
    success_url = reverse_lazy('custom_user_list')  # Redirige a la página principal después del registro --login--

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)


class UpdatePasswordView(UpdateView):
    model = CustomUser
    form_class = PasswordChangeForm
    template_name = 'administration/modificar_usuario.html'
    success_url = reverse_lazy('custom_user_list')  # Redirige a la página principal después de modificar la contraseña

    def get_object(self, queryset=None):
        user_id = self.kwargs.get('pk')
        user = get_object_or_404(CustomUser, pk=user_id)
        return user

    def get_form(self, form_class=None):
        return self.form_class(user=self.request.user, data=self.request.POST)

    def form_valid(self, form):
        user = form.save()
        update_session_auth_hash(self.request, user)  # Actualiza la sesión de autenticación después de cambiar la contraseña
        return super().form_valid(form)


class DeleteUserView(DeleteView):
    model = CustomUser
    template_name = 'administration/eliminar_usuario.html'  # Asegúrate de crear este template
    success_url = reverse_lazy('custom_user_list')  # Redirige a la página principal después de eliminar el usuario

    def get_object(self, queryset=None):
        user_id = self.kwargs.get('pk')
        user = get_object_or_404(CustomUser, pk=user_id)
        return user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        logout(request)  # Cierra la sesión del usuario antes de eliminarlo
        user.delete()  # Elimina al usuario
        return super().delete(request, *args, **kwargs)


# Vista para la listar los usuarios creados ....... creo jejejej
class CustomUserListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = get_user_model()
    template_name = 'administration/list_usuario.html'  # Replace with your template name
    context_object_name = 'users'

    def test_func(self):
        return self.request.user.is_superuser

        # Optionally, you can override the `handle_no_permission` method
        # to customize the redirect and message
    def handle_no_permission(self):
        messages.error(self.request, "No tienes permiso para ver esta página.")
        return redirect('index')


