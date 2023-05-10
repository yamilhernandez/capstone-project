from django import forms
from .models import Multa
from django.forms import ModelForm


class MultaForm(ModelForm):
    class Meta:
        required_css_class = 'required'
        model = Multa
        #'fecha_final','oficial', 'numero_compras', 'alerta'
        fields = ('num_caso', 'nombre_agencia', 'total', 'infraccion', 'pago') #'num_caso'

        labels = {
            'num_caso': 'ID del Caso',
            'nombre_agencia': 'Acrónimo de la Agencia',

            'total': 'Total a pagar:',
            'infraccion': 'Infracción',
            'pago': 'Pago?'
        }
        widgets = {
            'num_caso': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Inserte ID del caso.', 'style': 'margin-top:10px'}),
            'nombre_agencia': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Inserte Acrónimo de la Agencia.', 'width': '10px', 'style': 'margin-top:10px'}),


            'pago': forms.CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'Inserte agencia.', 'style': 'margin-top:10px'}),
            'total': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total a pagar', 'style': 'margin-top:10px'}),

            'infraccion':  forms.Select(attrs={'class': 'form-control', 'placeholder': 'Tipo de infracción.', 'style': 'margin-top:10px'})

        }
