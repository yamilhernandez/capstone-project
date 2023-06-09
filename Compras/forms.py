#from django_tables2 import tables, TemplateColumn
from django_tables2 import A
import django_tables2 as tables
from datetime import datetime
from django import forms
from .models import Compra
from django.forms import ModelForm
from django.utils.html import format_html
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, Row
from crispy_forms.bootstrap import PrependedAppendedText, InlineRadios
from django.core.paginator import Paginator

class CompraForm(ModelForm):

    class Meta:
        required_css_class = 'required'
        model = Compra
        fields = ['id_agencia', 'metodo', 'objeto', 'fecha_recibo', 'fecha_reporte','num_licitador',
                  'comentarios', 'comprador', 'num_compra', 'concepto', 'cantidad', 'fondos', 'descripcion', 
                  'id_comprador', 'asignacion', 'procedencia', 'proveedor', 'cuenta'] #'fecha_reporte'

        labels = {
            'id_agencia': 'ID Agencia',
            'metodo': 'Metodo',
            'objeto': 'Objeto',
            'num_licitador': '# Licitador:',
            'comentarios': 'Comentarios',
            #'fecha_reporte': 'Fecha de Reporte',
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
            'fecha_reporte': 'Fecha Reporte'
        }
        
        widgets = {

            'num_licitador' : 
                forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Inserte numero Licitador'}),

            'metodo': 
                forms.Select(attrs={'class': 'form-control', 'placeholder': 'Inserte metodo de compra.'}),

            'id_agencia': 
                forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte acrónimo de la agencia.'}),

            'objeto': 
                forms.Select(attrs={'class': 'form-control', 'placeholder': 'De ser delegada mencione el tipo.', 'id': 'objeto'}),

            'comentarios': 
                forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte comentarios.'}),

            'comprador': 
                forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte comprador.'}),

            'num_compra': 
                forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte numero de compra.'}),

            'concepto': 
                forms.Select(attrs={'class': 'form-control', 'placeholder' : 'Concepto de compra.', 'id': 'concepto'}),

            'cantidad': 
                forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total de Gastos'}),

            'fondos': 
                forms.RadioSelect(attrs={'class': 'form-control', 'placeholder': 'Tipo de fondo.'}),

            'descripcion': 
                forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ofrezca una descripcion.', 'id': 'descripcion'}),

            'id_comprador': 
                forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte  ID Comprador'}),

            'asignacion':  
                forms.Select(attrs={'class': 'form-control', 'placeholder': 'Inserte tipo de asignacion.', 'id': 'asignacion'}),

            'procedencia': 
                forms.Select(attrs={'class': 'form-control', 'placeholder': 'Inserte Procedencia.'}),

            'proveedor': 
                forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte nombre proveedor.'}),

            'cuenta': 
                forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte cifra de cuenta.'}),

            'fecha_recibo':
                forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'De ser delegada mencione el tipo.','type': 'date', 'max': datetime.now().date()}),

             'fecha_reporte':
                 forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'De ser delegada mencione el tipo.','type': 'date', 'max': datetime.now().date()}),

            # 'fecha_aprobacion':
            #     forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'De ser delegada mencione el tipo.','type': 'date', 'max': datetime.now().date()}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
  
        self.helper.layout = Layout(
            Row(
                Div(
                    'metodo', 'objeto', 'num_licitador',
                    PrependedAppendedText('cuenta', '$'),
                    'procedencia',
                    'descripcion',
                    css_class='col-md-4'
                ),
                Div(
                    'num_compra', 'asignacion',

                    PrependedAppendedText('cantidad', '$'),
                    'comentarios',
                    #'id_agencia',
                     InlineRadios('fondos'),
                    css_class='col-md-4'
                ),
                Div(
                    'fecha_reporte',
                    'concepto', 'fecha_recibo', 'comprador','proveedor',
                    #'id_comprador',
                    css_class='col-md-4'
                ),
            ),
            Submit('submit', 'Crear Compra', css_class='btn btn-secondary btn-primary letter container strong'),
        )

################################################################## TABLE CLASS ####################################################################################

class CheckBoxColumnWithName(tables.CheckBoxColumn):
    @property
    def header(self):
        return self.verbose_name

class SimpleTable(tables.Table):

    selection =  CheckBoxColumnWithName(verbose_name='Seleccione', accessor = 'id')
    """ Editar = tables.TemplateColumn('<a  style="float: leftmargin-left; margin-left: 20px;" href="{% url "editarcompra" record.compra_id %}"><i class="fas fa-pen" data-toggle="tooltip" data-placement="top" title="Editar Compra"></i></a>')#
    Partida = tables.TemplateColumn('<a  style="float: leftmargin-left; margin-left: 20px;" href="{% url "addpartida" record.compra_id %}"><i class="fas fa-plus" data-toggle="tooltip" data-placement="top" title="Crear Partida"></i></a>')#SE PUEDEN BORRA TAMBIEN """
    
    class Meta:
        model = Compra
        fields = ['selection','id_agencia' ,'metodo', 'objeto', 'fecha_recibo', 'fecha_reporte', 'num_licitador',
                  'comentarios', 'comprador', 'num_compra', 'concepto', 'cantidad', 'fondos', 'descripcion', 
                  'id_comprador', 'asignacion', 'procedencia', 'proveedor', 'cuenta'] # 'fecha_reporte'
        orderable = False
        attrs = {"class": "table table-sm table-striped"}
