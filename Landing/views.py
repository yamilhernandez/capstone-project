from django.utils.safestring import mark_safe
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from Agencias .models import Agencia
#from Casos .models import Caso
from Compras .models import Compra


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            username=username, password=password, request=request)

        if user is not None:
            auth.login(request, user)
            return redirect('/compras')
        else:
            return redirect('/indice')

    elif request.user.is_authenticated:
        return redirect('/compras')
    else:
        return render(request, 'login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required(login_url='login')
def indice(request):
    User = request.user.id
    # Print Username
    # print(User)
    agencias = Agencia.objects.order_by('acronimo')
    #casos = Caso.objects.order_by('nombre_agencia')
    compras = Compra.objects.order_by('comprador')
    context = {
        'agencias': agencias,
        #'casos': casos,
        'compras': compras,
    }
    if request.user.is_authenticated:
        if request.user.is_staff:
            agencias = Agencia.objects.all()
            #casos = Caso.objects.all()
            #compras = Compra.objects.all()
        else:
            # Filter agencies by oficial is equal to User logged in.
            agencias = Agencia.objects.filter(oficial=User)
            #casos = Caso.objects.filter(id_caso=User)
            #compras = Compra.objects.filter('comprador')

        context = {'agencias': agencias, 'compras': compras}
        return render(request, 'home/index.html', context)
    else:
        return render(request, 'home/index.html', context)
