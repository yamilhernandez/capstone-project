# Create your views here.
import django_tables2 as tables
from django.forms.models import model_to_dict
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from Agencias.models import Agencia
from .models import Compra
from django_tables2 import RequestConfig
from .forms import CompraForm, SimpleTable
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from datetime import date
# Create your views here.
Compras = []

#aqui esta funcion permite a~adir la compra
def AddCompra(request):
    submitted = False
    if request.method == "POST":
        form = CompraForm(request.POST, request.FILES)
        usuario = request.user.username

        if form.is_valid():

            f = form.save(commit=False)
            f.usuario = usuario
            f.save()
        else:
            print('error')
            print(form.errors)
            
        
        mensaje = ("Se creo la compra") #mensaje para indicar que se cero la compra
        messages.success(request, mensaje)
        submitted = True
        return render(request, 'home/Compras.html', {'form': form, 'submitted': submitted})

    else:
        form = CompraForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'home/Compras.html', {'form': form, 'submitted': submitted})





###########################muestra el form junto con la tabla #################################
def ComprasView(request):
    if request.method == "POST":
        data =  request.POST
        data._mutable = True
        data['id_comprador'] = request.user
        data['id_agencia'] = Agencia.objects.filter(oficial=request.user)[0]
        data._mutable = False
        form = CompraForm(data, request.FILES)
        if form.is_valid():

            form.save()

    form = CompraForm()
    if request.user.is_superuser:
        table = SimpleTable(Compra.objects.all())
    else:
        table = SimpleTable(Compra.objects.filter(id_comprador=request.user))
    table.paginate(page=request.GET.get("page", 1), per_page= 5)
    context = {'form': form, 'table' : table}
    return render(request, 'home/Compras.html', context)

#permite editar la compra, los campos connectados no aplican para client BORRAR LAS CRUD ORIGINALES
def EditarCompra(request, compra_id):
    
    compra = Compra.objects.get(compra_id = compra_id)
    form = CompraForm(instance=compra)

    if request.method == 'POST':
        form = CompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            return redirect('/compras')
    else:
        form = CompraForm(instance=compra)

    return render(request, 'home/ComprasEdit.html', {'form': form})


#esto elimina la compra
def EliminarCompra(request, compra_id):

    compra = Compra.objects.get(compra_id = compra_id)
    if request.method == 'POST':

        compra.delete()

        return redirect('/compras')

    return render(request, 'home/ComprasDelete.html', {'compra': compra})


#intento de a~adir partida
def AddPartida(request, compra_id):
    compra = Compra.objects.get(compra_id = compra_id)

    if request.method == 'POST':
        form = CompraForm(request.POST, request.FILES)
        form.save()
        return redirect('/compras')
    
    else:
        form = CompraForm(instance=compra)

    return render(request, 'home/AddPartida.html', {'form': form})





################SANDBOX hace redirect para limpiar el form y dejarlo incialmente#############################################

def clearAll(request):
    return redirect('/compras')

#####################Borrar por checkbox###########################

def deleteCHK(request):

    if request.method == 'POST':
        record_ids = request.POST.getlist('selection')
        if record_ids != []:
            print(record_ids)
            Compra.objects.filter(id__in=record_ids).delete()
            messages.success(request, 'Se Borró la compra seleccionada!')

    if record_ids == []:
        messages.success(request, "Seleccione una compra para borrar!")

        
    return redirect('/compras')
    
######################################################add partida por checkbox###########################

def partidaCHK(request):

    compra = Compra()

    if request.method == 'POST':
        data =  request.POST
        data._mutable = True
        data['id_comprador'] = request.user
        data['id_agencia'] = Agencia.objects.filter(oficial=request.user)[0]
        data._mutable = False
        form = CompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            messages.success(request, "Partida Añadida!")
            return redirect('/compras')

    else:
        record_ids = request.GET.getlist('selection')
        if record_ids == []:
            messages.success(request, "Seleccione una compra para añadir partida")
            return redirect('/compras')
        else:
            data =  request.POST
            data._mutable = True
            data['id_comprador'] = request.user
            data['id_agencia'] = Agencia.objects.filter(oficial=request.user)[0]
            data._mutable = False
            print(record_ids)
            compra = Compra.objects.get(id__in=record_ids)
            form = CompraForm(instance=compra)

    return render(request, 'home/AddPartida.html', {'form': form}) 

######################################################editar por checkbox#############################################

def editCHK(request):

    form = CompraForm()
    compra = Compra.objects.none()

    if request.method == 'POST':
        record_ids = request.GET.getlist('selection')
        print(record_ids)
        data =  request.POST
        data._mutable = True
        data['id_comprador'] = request.user
        data['id_agencia'] = Agencia.objects.filter(oficial=request.user)[0]
        data._mutable = False
        compra = Compra.objects.get(id__in=record_ids)
        form = CompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            print('saved!')
            messages.success(request, "Compra Editada!")
            return redirect('/compras')

    else:
        record_ids = request.GET.getlist('selection')
        if record_ids == []:
            messages.success(request, "Seleccione una compra para Editar")
            return redirect('/compras')
        
        else:
            data =  request.POST
            data._mutable = True
            data['id_comprador'] = request.user
            data['id_agencia'] = Agencia.objects.filter(oficial=request.user)[0]
            data._mutable = False
            #print(record_ids)
            compra = Compra.objects.get(id__in=record_ids)
            form = CompraForm(instance=compra)

    return render(request, 'home/ComprasEdit.html', {'form': form})
