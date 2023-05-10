from django import forms
from .models import Caso
from django.forms import ModelForm


class CasoForm(ModelForm):
    class Meta:
        required_css_class = 'required'
        model = Caso
        # 'fecha_final','oficial', 'numero_compras', 'alerta'
        fields = ('id_caso', 'nombre_agencia', 'estado', 'estatus')

        labels = {
            'id_caso': 'ID del Caso',
            'nombre_agencia': 'Nombre de la Agencia',

            'estado': 'Estado:',
            'estatus': 'Estatus',
        }
        widgets = {
            'id_caso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte el ID del Caso.', 'style': 'margin-top:10px'}),
            'nombre_agencia': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Escoja la Agencia.', 'width': '10px', 'style': 'margin-top:10px'}),


            'estado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Escoja en que estado se encuentra la agencia.', 'style': 'margin-top:10px'}),
            # 'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte propósito.', 'style': 'margin-top:10px'}),

            'estatus':  forms.CheckboxInput(attrs={'required': False, 'class': 'form-control', 'style': 'margin-top:10px', 'value': 'True', 'id': 'estatus', 'checked': 'False'})
        }