from django.shortcuts import render
from django.http import HttpResponse
from Compras.models import Compra
from Compras.forms import CompraForm
from CompraSometida.models import CompraSometida
from CompraSometida.forms import SometidaForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from datetime import date
# Create your views here.
# Create your views here.

#esto borra la compra de Compras y las somete en CompraSometida
def submitted(request, compra_id):

   compra = Compra.objects.get(compra_id = compra_id)

   if request.method == 'POST':
        form = SometidaForm(request.POST, request.FILES)
        form.save()
        compra.delete()
        return redirect('/compras')
        
   else:
      form = CompraForm(instance=compra)
   
   return render(request, 'home/CompraSometida.html', {'form': form}) #llama a compra sometida para realizar el submit

#view similar al de compras, pero este se llama sometida view
def sometidaView(request):
    compras = CompraSometida.objects.order_by('id_agencia')
    context = {'compras': compras}

    return render(request, 'home/sometidaView.html', context)


#obtiene la info y la muestra en el web, se elimino el boton de submit. 
def detailedView(request, compra_id):
    sometido = CompraSometida.objects.get(compra_id = compra_id)
    form = SometidaForm(instance=sometido)

    return render (request, 'home/CompraSometida.html', {'form': form})
