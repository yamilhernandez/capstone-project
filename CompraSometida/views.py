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

###############################################view similar al de compras, pero este se llama sometida view
def sometidaView(request):
    comprasometida = CompraSometida.objects.values('num_reporte')

    compras_por_reporte = {}
    for compra in comprasometida:
        num_reporte = compra['num_reporte']
        if num_reporte not in compras_por_reporte:
            compras_por_reporte[num_reporte] = []
        compras_por_reporte[num_reporte].extend(
            CompraSometida.objects.filter(num_reporte=num_reporte))

    context = {'compras_por_reporte': compras_por_reporte}
    return render(request, 'home/sometidaView.html', context)

#####################################Detailed View##########################################

def ComprasDetails(request, num_reporte):
    compras = CompraSometida.objects.filter(num_reporte=num_reporte)
    table = sometidaTable(compras)
    table.paginate(page=request.GET.get("page", 1), per_page= 8)
    context = {'table': table}
    return render(request, 'home/sometidaFiltrada.html', context)



############################SANDBOX para guardar y mostrar###################################

def submitAll(request):
    data = Compra.objects.all()
    num_reporte = request.POST.get('num_reporte')
    for compra in data:
        compra_data = model_to_dict(compra)
        compra_data.pop('id')
        compra_data['num_reporte'] = num_reporte
        CompraSometida.objects.create(**compra_data)

    Compra.objects.all().delete()
    sometida = CompraSometida.objects.all()
    context = {'form': {}, 'table': sometida}
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


###################################Filtrando compras sometidas por trimestre########################################################

def Q1(request):
    compra = CompraSometida.objects.filter(fecha_reporte__range = ('2023-01-01', '2023-03-31')).values()
    table = sometidaTable(compra)
    table.paginate(page=request.GET.get("page", 1), per_page= 8)
    context = {'table' : table}
    return render(request, 'home/sometidaFiltrada.html', context)

def Q2(request):
    compra = CompraSometida.objects.filter(fecha_reporte__range = ('2023-04-01', '2023-06-30')).values()
    table = sometidaTable(compra)
    table.paginate(page=request.GET.get("page", 1), per_page= 8)
    context = {'table' : table}
    return render(request, 'home/sometidaFiltradaQ2.html', context)

def Q3(request):
    compra = CompraSometida.objects.filter(fecha_reporte__range = ('2023-07-01', '2023-09-30')).values()
    table = sometidaTable(compra)
    table.paginate(page=request.GET.get("page", 1), per_page= 8)
    context = {'table' : table}
    return render(request, 'home/sometidaFiltradaQ3.html', context)

def Q4(request):
    compra = CompraSometida.objects.filter(fecha_reporte__range = ('2023-10-01', '2023-12-31')).values()
    table = sometidaTable(compra)
    table.paginate(page=request.GET.get("page", 1), per_page= 8)
    context = {'table' : table}
    return render(request, 'home/sometidaFiltradaQ4.html', context)