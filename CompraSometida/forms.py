from django import forms
from .models import CompraSometida
from django.forms import ModelForm
from datetime import datetime
from Compras.models import Compra
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, Row
from crispy_forms.bootstrap import PrependedAppendedText, InlineRadios
from django_tables2 import tables 
import itertools

class SometidaForm(ModelForm):
    class Meta:
        required_css_class = 'required'
        model = CompraSometida
        fields = ['id_agencia', 'metodo', 'objeto', 'fecha_reporte', 'fecha_recibo', 'num_licitador',
                  'comentarios', 'comprador', 'num_compra', 'concepto', 'cantidad', 'fondos', 'descripcion', 
                  'id_comprador', 'asignacion', 'procedencia', 'proveedor', 'cuenta', 'num_reporte']

        labels = {
            'id_agencia': 'ID Agencia',
            'metodo': 'Metodo',
            'objeto': 'Objeto',
            'num_licitador': '# Licitador:',
            'comentarios': 'Comentarios',
            'fecha_reporte': 'Fecha de Reporte',
            'num_compra': 'Numero de Compra',
            'cantidad': 'Cantidad Total de Gastos $',
            'fondos': 'Fondos',
            'descripcion': 'Descripcion',
            'id_comprador': 'ID Comprador',
            'asignacion': 'Asignacion',
            'procedencia': 'Procedencia',
            'proveedor': 'Proveedor',
            'cuenta': 'Cuenta',
            'comprador': 'Comprador',
            'fecha_recibo': 'Fecha Recibo',
            'num_reporte': 'Numero Reporte'
        }
        
        widgets = {

            'num_reporte' : 
                forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Numero Reporte'}),

            'num_licitador' : 
                forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Inserte numero Licitador'}),

            'metodo': 
                forms.Select(attrs={'class': 'form-control', 'placeholder': 'Inserte metodo de compra.'}),

            'id_agencia': 
                forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte acrónimo de la agencia.'}),

            'objeto': 
                forms.Select(attrs={'class': 'form-control', 'placeholder': 'De ser delegada mencione el tipo.'}),

            'comentarios': 
                forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte comentarios.'}),

            'comprador': 
                forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte comprador.'}),

            'num_compra': 
                forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte numero de compra.'}),

            'concepto': 
                forms.Select(attrs={'class': 'form-control', 'placeholder': 'Concepto de compra.'}),

            'cantidad': 
                forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total de Gastos'}),

            'fondos': 
                forms.RadioSelect(attrs={'class': 'form-control', 'placeholder': 'Tipo de fondo.'}),

            'descripcion': 
                forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ofrezca una descripcion.'}),

            'id_comprador': 
                forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte  ID Comprador'}),

            'asignacion':  
                forms.Select(attrs={'class': 'form-control', 'placeholder': 'Inserte tipo de asignacion.'}),

            'procedencia': 
                forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte Procedencia.'}),

            'proveedor': 
                forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte nombre proveedor.'}),

            'cuenta': 
                forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte cifra de cuenta.'}),

            'fecha_recibo':
                forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'De ser delegada mencione el tipo.','type': 'date', 'max': datetime.now().date()}),

            'fecha_reporte':
                forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'De ser delegada mencione el tipo.','type': 'date', 'max': datetime.now().date()}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
  
        self.helper.layout = Layout(
            Row(
                Div(
                    'metodo', 'objeto', 'num_licitador',
                    PrependedAppendedText('cuenta', '$', '.00'),
                    'procedencia',
                    'descripcion',
                    css_class='col-md-4'
                ),
                Div(
                    'num_compra', 'asignacion',
                    PrependedAppendedText('cantidad', '$', '.00'),
                    'comentarios',
                    'id_agencia',
                     InlineRadios('fondos'),
                    css_class='col-md-4'
                ),
                Div(
                    'fecha_reporte','concepto', 'fecha_recibo', 'comprador','proveedor',
                    'id_comprador',
                    css_class='col-md-4'
                ),
            ),
            #Submit('submit', 'Someter Compra', css_class='button white btn-block mt-3'),
        )

class sometidaTable(tables.Table):

    class Meta:
        model = CompraSometida
        exclude = ('id', 'compra_id')
        orderable = False
        attrs = {"class": "table table-sm table-striped"}

        def render_descripcion(self, value):
            all_choices = CompraSometida.description
            dictionnary = {i[0]:i[1] for i in all_choices}
            return f"{dictionnary[value]}"
        
        def render_concepto(self, value):
            all_choices = CompraSometida.descriptionAssign
            dictionnary = {i[0]:i[1] for i in all_choices}
            return f"{dictionnary[value]}"
        
        def render_metodo(self, value):
            all_choices = CompraSometida.method_type
            dictionnary = {i[0]:i[1] for i in all_choices}
            return f"{dictionnary[value]}"
#autodate
#duplicate compras 