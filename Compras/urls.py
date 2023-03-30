from django.urls import path
from Compras import views
from django.contrib import admin

from .views import (ComprasView, AddCompra, EliminarCompra, EditarCompra)

#app_name = 'Compras'
urlpatterns = [

    path('', ComprasView, name='compra'),
    path('addcompra', views.AddCompra, name='addcompra'),
    path('eliminarcompra/<compra_id>', views.EliminarCompra, name='eliminarcompra'),
    path('editarcompra/<compra_id>', views.EditarCompra, name='editarcompra'),
    #path('testcompra', views.testCompra, name='test'),

]
