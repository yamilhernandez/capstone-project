from django.contrib import admin
from django.urls import include, path, re_path
from .views import (login,indice,logout)

urlpatterns = [
    
    path('', login, name="login"),
    path('login', login, name="login"),
    path('indice', indice, name = "indice"),
    path('logout', logout, name='logout')

]
