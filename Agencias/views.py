#from typing import Self
from django.shortcuts import render
from django.http import HttpResponse
from .models import Agencia, Usuario
from .forms import AgenciaForm

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth import get_user_model

from datetime import date
# Create your views here.

Agencias = []


def AddAgencia(request):

    submitted = False
    if request.method == "POST":
        form = AgenciaForm(request.POST, request.FILES)
        usuario = request.user.username

        if form.is_valid():

            f = form.save(commit=False)
            f.usuario = usuario
            f.save()

        messages.success(request, "Se añadió un nuevo comunicado.")
        return HttpResponseRedirect('agenciasAddAgencia?submitted=True')

    else:
        form = AgenciaForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'home/AddAgencia.html', {'form': form, 'submitted': submitted})


def AgenciasView(request):
    # Get username
    User = request.user.id
    #user = Usuario.objects.get(nombre=User)
    #Usuario = Usuario.objects.get(oficial='Nombre')

    # Print Username
    # print(User)

    agencias = Agencia.objects.order_by('acronimo')
    context = {'agencias': agencias}
    if request.user.is_authenticated:
        if request.user.is_staff:
            agencias = Agencia.objects.all()
        else:
            # Filter agencies by oficial is equal to User logged in.

            agencias = Agencia.objects.filter(oficial=User)

        context = {'agencias': agencias}
        return render(request, 'home/Agencias.html', context)
    else:

        return render(request, 'home/Agencias.html', context)


def EditarAgencia(request, agencia_id=None):
    submitted = False
    if request.method == "POST":

        form = AgenciaForm(request.POST)

        acronimo = request.POST['acronimo']
        nombre = request.POST['nombre']
        categoria = request.POST['categoria']
        tipo = request.POST['tipo']

        # Fecha de inicio
        fecha_inicio_day = request.POST.get('fecha_inicio_day')
        fecha_inicio_month = request.POST.get('fecha_inicio_month')
        fecha_inicio_year = request.POST.get('fecha_inicio_year')

        # Fecha Final
        fecha_final_day = request.POST.get('fecha_final_day')
        fecha_final_month = request.POST.get('fecha_final_month')
        fecha_final_year = request.POST.get('fecha_final_year')

        usuario = request.POST.get('usuario')
        #numero_compras = request.POST['numero_compras']
        alerta = request.POST['alerta']
        #image_agencia = request.POST['image_agencia']

        agencia = Agencia.objects.get(agencia_id=agencia_id)
        #agencia.image_agencia = image_agencia
        agencia.acronimo = acronimo
        agencia.nombre = nombre
        agencia.agencia = agencia
        agencia.categoria = categoria
        agencia.tipo = tipo

        agencia.fecha_inicio = agencia.fecha_inicio.replace(day=int(
            fecha_inicio_day), month=int(fecha_inicio_month), year=int(fecha_inicio_year))
        agencia.fecha_final = agencia.fecha_final.replace(day=int(
            fecha_final_day), month=int(fecha_final_month), year=int(fecha_final_year))

        agencia.usuario = usuario
        #agencia.numero_compra = numero_compras
        agencia.alerta = alerta
        agencia.save()

        message = ('La agencia se enmendó ')
        messages.success(request, message)
        submitted = True
        return render(request, 'home/AgenciasEdit.html', {'agencia': agencia, 'submitted': submitted})

    else:
        agencia = Agencia.objects.get(agencia_id=agencia_id)
        form = AgenciaForm(request.POST or None, instance=agencia)

        return render(request, 'home/AgenciasEdit.html', {'form': form, 'agencia': agencia, 'submitted': submitted})


def EliminarAgencia(request, agencia_id=None):

    agencia = Agencia.objects.get(agencia_id=agencia_id)
    if request.method == 'POST':

        agencia.delete()

        return redirect('/agencias')

    return render(request, 'home/AgenciasDelete.html', {'agencia': agencia})
