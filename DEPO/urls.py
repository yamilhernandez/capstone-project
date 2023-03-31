from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('Landing.urls')),
    path('admin/', admin.site.urls),
    path('agencias', include('Agencias.urls')),
    path('usuarios', include('Usuarios.urls')),
    #path('casos', include('Casos.urls')),
    #path('hallazgos', include('Hallazgos.urls')),
    path('compras', include('Compras.urls')),
    path('comprasometida', include('CompraSometida.urls')),
    #path('multas', include('Multas.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
