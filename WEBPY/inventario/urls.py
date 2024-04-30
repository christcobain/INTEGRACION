from django.urls import path
from .views import register_view,index,login_view,about_view, logout_view

urlpatterns = [
    path('',index,name='index'),
    path('registro/', register_view, name='registro'),
    path('login/', login_view, name='login'),
    path('about/', about_view,name='about'),
    path('about/', about_view,name='home'),
    path('logout/', logout_view, name='logout'),
]