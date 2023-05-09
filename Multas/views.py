from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Multa
from .forms import MultaForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

#from datetime import date
# Create your views here.

Multas = []


def AddMulta(request):

    submitted = False
    if request.method == "POST":
        form = MultaForm(request.POST, request.FILES)
        usuario = request.user.username

        if form.is_valid():

            f = form.save(commit=False)
            f.usuario = usuario
            f.save()

        messages.success(request, "Se añadió una nueva multa.")
        return HttpResponseRedirect('multasAddMulta?submitted=True')

    else:
        form = MultaForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'home/AddMulta.html', {'form': form, 'submitted': submitted})


def MultasView(request):

    User = request.user.id
    multas = Multa.objects.order_by('nombre_agencia')
    context = {'multas': multas}

    if request.user.is_authenticated:
        if request.user.is_staff:
            multas = Multa.objects.all()
        else:
            # Filter agencies by oficial is equal to User logged in.
            multas = Multa.objects.filter(nombre_agencia=User)

        context = {'multas': multas}
        return render(request, 'home/Multas.html', context)
    else:

        return render(request, 'home/Multas.html', context)


def EditarMulta(request, multa_id=None):
    submitted = False
    if request.method == "POST":

        form = MultaForm(request.POST)

       # id_multa = request.POST['id_multa']
        nombre_agencia = request.POST['nombre_agencia']
        #num_caso = request.POST['num_caso']
        total = request.POST['total']
        infraccion = request.POST['infraccion']
        pago = request.POST['pago']

        multa = Multa.objects.get(multa_id=multa_id)
       #multa.id_multa = id_multa
        multa.nombre_agencia = nombre_agencia
        #multa.num_caso = num_caso
        multa.total = total
        multa.infraccion = infraccion
        multa.pago = pago

        multa.save()

        message = ('El caso se creo')
        messages.success(request, message)
        submitted = True
        return render(request, 'home/MultasEdit.html', {'multa': multa, 'submitted': submitted})

    else:
        multa = Multa.objects.get(multa_id=multa_id)
        form = MultaForm(request.POST or None, instance=multa)

        return render(request, 'home/MultasEdit.html', {'form': form, 'multa': multa, 'submitted': submitted})


def EliminarMulta(request, multa_id=None):

    multa = Multa.objects.get(multa_id=multa_id)
    if request.method == 'POST':

        multa.delete()

        return redirect('/multas')

    return render(request, 'home/MultasDelete.html', {'multa': multa})
