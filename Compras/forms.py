from datetime import datetime
from django import forms
from .models import Compra
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, Row
from crispy_forms.bootstrap import PrependedAppendedText, InlineRadios
class CompraForm(ModelForm):

    class Meta:
        required_css_class = 'required'
        model = Compra
        fields = ['id_agencia', 'metodo', 'objeto', 'fecha_reporte', 'fecha_recibo', 'num_licitador',
                  'comentarios', 'comprador', 'num_compra', 'concepto', 'cantidad', 'fondos', 'descripcion', 
                  'id_comprador', 'asignacion', 'procedencia', 'proveedor', 'cuenta']

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
            'fecha_recibo': 'Fecha Recibo'
        }
        
        widgets = {
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
            Submit('submit', 'Crear Compra', css_class='button white btn-block mt-3'),
        )



#autodate
#duplicate compras 