from django.urls import path
from CompraSometida import views
from django.contrib import admin

from .views import submitted

#app_name = 'Compras'
urlpatterns = [

    path('sometido/<compra_id>', views.submitted, name='sometido')

]