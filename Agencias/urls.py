from django.urls import path

from .views import (AgenciasView, AddAgencia, EliminarAgencia, EditarAgencia)

app_name = 'Agencias'
urlpatterns = [

    path('', AgenciasView, name='agencia'),
    path('AddAgencia', AddAgencia, name='addagencia'),
    path('eliminaragencia/<agencia_id>',
         EliminarAgencia, name='eliminaragenica'),
    path('editaragencia/<agencia_id>', EditarAgencia, name='editaragencia'),



]
