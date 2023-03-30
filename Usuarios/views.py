from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from .forms import UsuarioForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

#from datetime import date
# Create your views here.

Usuarios = []


def AddUsuario(request):

    submitted = False
    if request.method == "POST":
        form = UsuarioForm(request.POST, request.FILES)
        usuario = request.user.username

        if form.is_valid():

            f = form.save(commit=False)
            f.usuario = usuario

            f.save()

        messages.success(request, "Se añadió un nuevo usuario.")
        return HttpResponseRedirect('usuariosAddUsuario?submitted=True')

    else:
        form = UsuarioForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'home/AddUsuario.html', {'form': form, 'submitted': submitted})


def UsuariosView(request):
    usuarios = Usuario.objects.order_by('nombre')

    # if (usuario is admin){
    #    agencias = Agencias.objects.all()
    # }else{
    #     agencias = Agencias.objects.filter(agencias = usuarioAgencias)
    # }
    context = {'usuarios': usuarios}

    return render(request, 'home/Usuarios.html', context)


def EditarUsuario(request, usuario_id=None):
    submitted = False
    if request.method == "POST":

        form = UsuarioForm(request.POST)

        puesto = request.POST['puesto']
        nombre = request.POST['nombre']
        extension = request.POST['extension']
        Rol = request.POST['Rol']

        # Fecha de inicio
        #fecha_inicio_day = request.POST.get('fecha_inicio_day')
        #fecha_inicio_month = request.POST.get('fecha_inicio_month')
        #fecha_inicio_year = request.POST.get('fecha_inicio_year')

        # Fecha Final
        #fecha_final_day = request.POST.get('fecha_final_day')
        #fecha_final_month = request.POST.get('fecha_final_month')
        #fecha_final_year= request.POST.get('fecha_final_year')

        #oficial = request.POST.get('oficial')
        #numero_compras = request.POST['numero_compras']
        #alerta = request.POST['alerta']

        usuario = Usuario.objects.get(usuario_id=usuario_id)

        usuario.puesto = puesto
        usuario.nombre = nombre
        usuario.extension = extension
        usuario.Rol = Rol

        #usuario.tipo = tipo

        #agencia.fecha_inicio = agencia.fecha_inicio.replace(day=int(fecha_inicio_day), month=int(fecha_inicio_month), year=int(fecha_inicio_year))
        #agencia.fecha_final = agencia.fecha_final.replace(day=int(fecha_final_day), month=int(fecha_final_month), year=int(fecha_final_year))

        #agencia.oficial = oficial
        #gencia.numero_compra = numero_compras
        #agencia.alerta = alerta
        usuario.save()

        message = ('El usuario se creo')
        messages.success(request, message)
        submitted = True
        return render(request, 'home/UsuariosEdit.html', {'usuario': usuario, 'submitted': submitted})

    else:
        usuario = Usuario.objects.get(usuario_id=usuario_id)
        form = UsuarioForm(request.POST or None, instance=usuario)

        return render(request, 'home/UsuariosEdit.html', {'form': form, 'usuario': usuario, 'submitted': submitted})


def EliminarUsuario(request, usuario_id=None):

    usuario = Usuario.objects.get(usuario_id=usuario_id)
    if request.method == 'POST':

        usuario.delete()

        return redirect('/usuarios')

    return render(request, 'home/UsuariosDelete.html', {'usuario': usuario})
