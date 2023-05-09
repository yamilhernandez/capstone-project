from django.urls import path

from .views import (MultasView, AddMulta, EliminarMulta, EditarMulta)
from Multas import views

#app_name = 'Multas'
urlpatterns = [

    path('', MultasView, name='multa'),
    path('AddMulta', AddMulta, name='addmulta'),
    path('eliminarmulta/<multa_id>', EliminarMulta, name='eliminarmulta'),
    path('editarmulta/<multa_id>', EditarMulta, name='editarmulta')



]
