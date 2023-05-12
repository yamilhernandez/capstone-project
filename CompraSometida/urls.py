from django.urls import path
from CompraSometida import views
from django.contrib import admin

from .views import (submitted, sometidaView,submitAll, deleteAll, Q1, Q2, ComprasDetails)

#app_name = 'Compras'
urlpatterns = [

    path('sometido', views.submitted, name='sometido'),
    path('sometida', views.sometidaView, name='sometida'),
    path('submitAll', views.submitAll, name='submitAll'),
    path('deleteAll', views.deleteAll, name='deleteAll'),
    path('Comprasdetails/<num_reporte>', views.ComprasDetails, name='ComprasDetails'),
    path('Q1', views.Q1, name='Q1'),
    path('Q2', views.Q2, name='Q2'),
    path('Q3', views.Q3, name='Q3'),
    path('Q4', views.Q4, name='Q4')

    #los htmls intente ponerles la palabra sometido para identidficar.
]