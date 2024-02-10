from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


class Inicio(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


# =======================================================================================================================



# =======================================================================================================================

#   <!-- ======= Vistas de crear expedientes ======= -->

def crear_expedientes(request):
    return render(request, 'expedientes/crear_expedientes.html')
