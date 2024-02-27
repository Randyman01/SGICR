from django.urls import path
from app.sgicr.views import Inicio
from . import views

urlpatterns = [
    path('', Inicio.as_view(), name='index'),


#   <!-- ======= Urls Vistas de Usuario ======= -->
#    path('usuarios/', views.lista_usuarios, name='lista_usuario'),
#    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
#    path('usuarios/modificar/<int:id>/', modificar_usuario, name='modificar_usuario'),
#    path('usuarios/eliminar/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),
#   <!-- ======= End Urls Vistas de Usuario ======= -->

#   <!-- ======= Urls Vistas Expedientes ======= -->
    path('expedientes/crear/', views.crear_expedientes, name='crear_expedientes'),
#   <!-- ======= End Urls Vistas Expedientes ======= -->
]