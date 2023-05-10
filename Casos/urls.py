from django.urls import path
from . import views


from .views import (CasosView, AddCaso, EliminarCaso, EditarCaso, DetailCaso)

app_name = 'Casos'
urlpatterns = [

    path('', CasosView, name='caso'),
    path('AddCaso', AddCaso, name='addcaso'),
    path('eliminarcaso/<caso_id>',
         EliminarCaso, name='eliminarcaso'),
    path('editarcaso/<caso_id>', EditarCaso, name='editarcaso'),
    path('detailscaso/<caso_id>/', DetailCaso, name='detailscaso'),
]