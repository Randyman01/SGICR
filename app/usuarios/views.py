from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.contrib.auth import authenticate
from .forms import UserLoginForm
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.views.generic import ListView
from django.contrib import messages


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
    success_url = reverse_lazy('login')  # Redirige a la página principal después del registro

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Autenticar al usuario después de registrarse
        return super().form_valid(form)


class CustomUserListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = get_user_model()
    template_name = 'administration/list_usuario.html'  # Replace with your template name
    context_object_name = 'users'

    def test_func(self):
        return self.request.user.is_superuser

        # Optionally, you can override the `handle_no_permission` method
        # to customize the redirect and message
    def handle_no_permission(self):
        messages.error(self.request, "You do not have permission to view this page.")
        return redirect('index')



