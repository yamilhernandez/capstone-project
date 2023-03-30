from django import forms
from .models import Agencia
from django.forms import ModelForm


class AgenciaForm(ModelForm):
    class Meta:
        required_css_class = 'required'
        model = Agencia
        fields = ('acronimo', 'nombre', 'categoria', 'tipo', 'fecha_inicio', 'fecha_final',
                  'oficial', 'image_agencia', 'alerta')

        labels = {
            'acronimo': 'Acrónimo',
            'nombre': 'Nombre de Agencia',
            'categoria': 'Categoría',
            'tipo': 'Tipo:',
            'oficial': 'Oficial',
            'fecha_inicio': 'Fecha Inicial',
            'fecha_final': 'Fecha Final',
            'image_agencia': 'Imagen Agencia',
            # 'numero_compras': 'Numero Compra',
            'alerta': 'Alerta',
        }
        widgets = {
            'acronimo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte acrónimo de la agencia.', 'width': '10px', 'style': 'margin-top:10px'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte nombre de la agencia.', 'style': 'margin-top:10px'}),
            'categoria': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Escoja si la agencia es delegada o exenta.', 'style': 'margin-top:10px'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'De ser delegada mencione el tipo.', 'style': 'margin-top:10px'}),
            'oficial': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Oficial a cargo.', 'style': 'margin-top:10px'}),
            'fecha_inicio': forms.SelectDateWidget(years=range(2015, 2030), attrs={'class': 'form-control', 'placeholder': 'Escoja una fecha', 'style': 'margin-top:10px'}),
            'fecha_final': forms.SelectDateWidget(years=range(2015, 2030), attrs={'class': 'form-control', 'placeholder': 'Escoja una fecha', 'style': 'margin-top:10px'}),
            'image_agencia': forms.ClearableFileInput(attrs={'class': 'form-control', 'type': 'file', 'id': 'formFile', 'placeholder': 'Seleccione imagen de la agencia', 'multiple': True, 'style': 'margin-top:10px'}),
            # 'numero_compras': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte propósito.', 'style': 'margin-top:10px'}),
            'alerta':  forms.CheckboxInput

        }
