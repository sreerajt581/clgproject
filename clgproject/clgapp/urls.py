from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.home,name='home.html'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('newpage',views.newpage,name='newpage'),


]