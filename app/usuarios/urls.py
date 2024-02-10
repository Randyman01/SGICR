from django.contrib.auth.views import LogoutView
from django.urls import path,include
from .views import LoginView, RegisterUserView, CustomUserListView

urlpatterns = [

    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
    path('users/', CustomUserListView.as_view(), name='custom_user_list'),

     # Otras URLs de tu aplicación
]
