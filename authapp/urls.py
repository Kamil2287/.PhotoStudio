from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/register', views.register, name="register"),
    path('auth/register2', views.register, name="register2"),
    path('auth/login', views.login, name="login"),
]
