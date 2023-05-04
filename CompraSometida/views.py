from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict
from Compras.models import Compra
from Compras.forms import CompraForm,SimpleTable
from CompraSometida.models import CompraSometida
from CompraSometida.forms import SometidaForm, sometidaTable
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from Compras.forms import SimpleTable
import django_tables2 as tables
from django_tables2 import RequestConfig
from django.core.paginator import Paginator
from datetime import date
# Create your views here.
# Create your views here.

#esto borra la compra de Compras y las somete en CompraSometida ####Intento 2
def submitted(request):

   compra = Compra.objects.all()
   table = sometidaTable(compra)
   if request.method == 'POST':
        form = SometidaForm(request.POST, request.FILES)
        form.save()
        compra.delete()
        return redirect('/compras')
   
   return render(request, 'home/CompraSometida.html', {'form': form, 'table': table}) #llama a compra sometida para realizar el submit """

#view similar al de compras, pero este se llama sometida view
def sometidaView(request):
    table = sometidaTable(CompraSometida.objects.all())
    table.paginate(page=request.GET.get("page", 1), per_page= 5)
    context = {'table' : table}
    return render(request, 'home/sometidaView.html', context)


#obtiene la info y la muestra en el web, se elimino el boton de submit. BORRAR
def detailedView(request, compra_id):
    sometido = CompraSometida.objects.get(compra_id = compra_id)
    form = SometidaForm(instance=sometido)

    return render (request, 'home/CompraSometida.html', {'form': form})


############################SANDBOX para guardar y mostrar###################################

def submitAll(request):
    data = Compra.objects.all()

    for compra in data:
        compra_data = model_to_dict(compra)
        compra_data.pop('id')
        CompraSometida.objects.create(**compra_data)

    Compra.objects.all().delete()
    context = {'form': {}, 'table': data}

    return render(request, 'home/sometidaView.html', context)

####################sandbox para eliminar todas############################################
def deleteAll(request):
    data = Compra.objects.all()

    Compra.objects.all().delete()
    context = {'form': {}, 'table': data}
    return redirect('/compras')

############################################################################################ BORRAR
def save_ids(compra_ids):
    for compra_id in compra_ids:
        compra_sometida = CompraSometida(id=compra_id)
        compra_sometida.save()
