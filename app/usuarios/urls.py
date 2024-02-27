from django.contrib.auth.views import LogoutView
from django.urls import path,include
from .views import LoginView, RegisterUserView, CustomUserListView, UpdatePasswordView, \
    DeleteUserView  # , EliminarUsuarioView

urlpatterns = [

    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
    path('users/', CustomUserListView.as_view(), name='custom_user_list'),
    path('updateuser/<int:pk>', UpdatePasswordView.as_view(), name='modificar_usuario'),
    path('deleteuser/<int:pk>', DeleteUserView.as_view(), name='eliminar_usuario'),

     # Otras URLs de tu aplicación
]
