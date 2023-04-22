from django.urls import path
from CompraSometida import views
from django.contrib import admin

from .views import (submitted, sometidaView, detailedView,submitID)

#app_name = 'Compras'
urlpatterns = [

    path('sometido', views.submitted, name='sometido'),
    path('sometida', views.sometidaView, name='sometida'),
    path('detallado/<compra_id>', views.detailedView, name='detallado'),#esto es para llamar todo lo que tenga que ver con los sometidos
    path('submitID', views.submitID, name='submit') 
    #los htmls intente ponerles la palabra sometido para identidficar.
]