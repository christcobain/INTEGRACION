from re import template
from django.urls import path
from django.contrib.auth import views as autentication_views
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('register/', views.register,name='register'),
    path('login/', autentication_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/', autentication_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('about/', views.about,name='about'),
    path('products/',views.products,name='products'),
    path('create_products/',views.create_product,name='create_products'),
]
