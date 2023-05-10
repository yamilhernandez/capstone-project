from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from Agencias.models import Agencia
from .models import Caso
from .forms import CasoForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.templatetags.static import static
from django.contrib.auth.models import User

#from datetime import date
# Create your views here.

Casos = []


def AddCaso(request):

    submitted = False
    if request.method == "POST":
        form = CasoForm(request.POST, request.FILES)
        usuario = request.user.id

        if form.is_valid():

            f = form.save(commit=False)
            f.usuario = usuario
            f.save()

        messages.success(request, "Se añadió un nuevo caso.")
        return HttpResponseRedirect('casosAddCaso?submitted=True')

    else:
        form = CasoForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'home/AddCaso.html', {'form': form, 'submitted': submitted})


def CasosView(request):

    User = request.user.id
    distinct_emails = Agencia.objects.values_list(
        'oficial__email', flat=True).distinct()

    filtro = request.GET.get('filtro', '')
    casos = Caso.objects.order_by('nombre_agencia')
    context = {'casos': casos, 'distinct_emails': distinct_emails}

    if request.method == "POST":

        if (request.POST.get("search") != None):
            search = request.POST.get("search")

            casos = (Caso.objects.filter(nombre_agencia__acronimo__icontains=search)) or (
                Caso.objects.filter(id_caso__icontains=search)) or (Caso.objects.filter(nombre_agencia_nombre_icontains=search))

            context = {'casos': casos}
            return render(request, 'home/Casos.html', context)
    else:
        casos = Caso.objects.all()
        context = {'casos': casos}

    if filtro and filtro in distinct_emails:
        casos = Caso.objects.filter(nombre_agencia__oficial__email=filtro)
        context = {'casos': casos, 'distinct_emails': distinct_emails}
        return render(request, 'home/Casos.html', context)

    if request.user.is_authenticated:
        if request.user.is_staff:
            casos = Caso.objects.all()
        else:
            # Filter agencies by oficial is equal to User logged in.
            if User:
                casos = Caso.objects.filter(nombre_agencia__oficial=User)
            else:
                casos = Caso.objects.none()

        context = {'casos': casos, 'distinct_emails': distinct_emails}
        return render(request, 'home/Casos.html', context)
    else:
        return render(request, 'home/Casos.html', context)


def EditarCaso(request, caso_id=None):
    submitted = False
    if request.method == "POST":

        form = CasoForm(request.POST)

        id_caso = request.POST['id_caso']
        #nombre_agencia = request.POST['nombre_agencia']

        estado = request.POST['estado']

        estatus = request.POST.get('estatus')

        caso = Caso.objects.get(caso_id=caso_id)

        caso.id_caso = id_caso

        caso.estado = estado
        caso.estatus = estatus
        if form.is_valid():

            # caso = form.save(commit=False) # SI PONGO ESO AHÍ CREA UNA COPIA DE LO QUE ESTABA ANTES

            # Obtener el objeto Agencia correspondiente al objeto Caso
            agencia = Agencia.objects.get(pk=caso.nombre_agencia.pk)

            # Actualizar el campo alerta del objeto Agencia según el valor del campo estatus del objeto Caso
            agencia.alerta = caso.estatus
            agencia.save()

            caso.save()
            caso = form.save(commit=False)
            message = ('El caso se editó')
            messages.success(request, message)
            submitted = True
            return render(request, 'home/CasosEdit.html', {'caso': caso, 'submitted': submitted})

    else:
        caso = Caso.objects.get(caso_id=caso_id)
        form = CasoForm(request.POST or None, instance=caso)

        return render(request, 'home/CasosEdit.html', {'form': form, 'caso': caso, 'submitted': submitted})


def EliminarCaso(request, caso_id=None):

    caso = Caso.objects.get(caso_id=caso_id)
    if request.method == 'POST':

        caso.delete()

        return redirect('/casos')

    return render(request, 'home/CasosDelete.html', {'caso': caso})


def DetailCaso(request, caso_id=None):

    caso = Caso.objects.get(caso_id=caso_id)

    return render(request, 'home/DetailsCaso.html', {'caso': caso})