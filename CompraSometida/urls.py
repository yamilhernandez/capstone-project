from django.urls import path
from CompraSometida import views
from django.contrib import admin

from .views import (submitted, sometidaView, detailedView,submitAll, deleteAll)

#app_name = 'Compras'
urlpatterns = [

    path('sometido', views.submitted, name='sometido'),
    path('sometida', views.sometidaView, name='sometida'),
    path('detallado', views.detailedView, name='detallado'),# borrar
    path('submitAll', views.submitAll, name='submitAll'),
    path('deleteAll', views.deleteAll, name='deleteAll') 
    #los htmls intente ponerles la palabra sometido para identidficar.
]