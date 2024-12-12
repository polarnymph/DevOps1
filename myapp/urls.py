# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_redirect, name='home'),  # Редирект с главной страницы на login
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('success/', views.success_view, name='success'),
]
