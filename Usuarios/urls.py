from django.urls import path

from .views import (UsuariosView, AddUsuario, EliminarUsuario, EditarUsuario)

app_name = 'Usuarios'
urlpatterns = [

    path('', UsuariosView, name='usuario'),
    path('AddUsuario', AddUsuario, name='addusuario'),
    path('eliminarusuario/<usuario_id>',
         EliminarUsuario, name='eliminarusuario'),
    path('editarusuario/<usuario_id>', EditarUsuario, name='editarusuario'),



]
