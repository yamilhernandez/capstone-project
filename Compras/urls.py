from django.urls import path
from Compras import views
from django.contrib import admin

from .views import (ComprasView, AddCompra, EliminarCompra, EditarCompra, clearAll, deleteCHK, partidaCHK, editCHK)

#app_name = 'Compras'
urlpatterns = [

    path('', views.ComprasView, name='compra'),
    path('addcompra', views.AddCompra, name='addcompra'),
    path('eliminarcompra/<compra_id>', views.EliminarCompra, name='eliminarcompra'), #ELIMINAR CRUDS INICIALES
    path('editarcompra/<compra_id>', views.EditarCompra, name='editarcompra'),
    path('addpartida/<compra_id>', views.AddPartida, name='addpartida'),
    path('clearAll', views.clearAll, name='clearAll'),
    path('deleteCHK', views.deleteCHK, name='deleteCHK'),
    path('partidaCHK', views.partidaCHK, name='partidaCHK'),
    path('editCHK', views.editCHK, name='editCHK')

    
]
