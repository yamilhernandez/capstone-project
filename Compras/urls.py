from django.urls import path
from Compras import views
from django.contrib import admin

from .views import (ComprasView, AddCompra, EliminarCompra, EditarCompra)

#app_name = 'Compras'
urlpatterns = [

    path('', views.ComprasView, name='compra'),
    path('addcompra', views.AddCompra, name='addcompra'),
    path('eliminarcompra/<compra_id>', views.EliminarCompra, name='eliminarcompra'),
    path('editarcompra/<compra_id>', views.EditarCompra, name='editarcompra'),
    path('addpartida/<compra_id>', views.AddPartida, name='addpartida'),
    #path('listView', listView, name='listview'),

    #path('testcompra', views.testCompra, name='test'),

]
