from django.urls import path
from CompraSometida import views
from django.contrib import admin

from .views import (submitted, sometidaView,submitAll, deleteAll)

#app_name = 'Compras'
urlpatterns = [

    path('sometido', views.submitted, name='sometido'),
    path('sometida', views.sometidaView, name='sometida'),
    path('submitAll', views.submitAll, name='submitAll'),
    path('deleteAll', views.deleteAll, name='deleteAll') 
    #los htmls intente ponerles la palabra sometido para identidficar.
]