from django import forms
from .models import Usuario
from django.forms import ModelForm


class UsuarioForm(ModelForm):
    class Meta:
        required_css_class = 'required'
        model = Usuario
        # 'fecha_final','oficial', 'numero_compras', 'alerta'
        fields = ('puesto', 'nombre', 'extension', 'Rol', 'email')

        labels = {
            'puesto': 'Puesto',
            'nombre': 'Nombre',
            'extension': 'Extension',
            'Rol': 'Rol:',
            'email': 'email',
            # 'fecha_inicio':'Fecha Inicial',
            # 'fecha_final':'Fecha Final',
            # 'numero_compras': 'Numero Compra',
            # 'alerta': 'Alerta',
        }
        widgets = {
            'puesto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte descripción de subasta.', 'style': 'margin-top:10px'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte número de subasta.', 'width': '10px', 'style': 'margin-top:10px'}),

            'extension': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escoja tipo de subasta.', 'style': 'margin-top:10px'}),
            'Rol': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Inserte agencia.', 'style': 'margin-top:10px'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte propósito.', 'style': 'margin-top:10px'}),
            # 'fecha_inicio': forms.SelectDateWidget(years=range(2015, 2030) ,attrs={'class':'form-control', 'placeholder':'Escoja una fecha','style':'margin-top:10px'}),
            # 'fecha_final': forms.SelectDateWidget(years=range(2015, 2030) ,attrs={'class':'form-control', 'placeholder':'Escoja una fecha','style':'margin-top:10px'}),
            # 'numero_compras': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte propósito.', 'style': 'margin-top:10px'}),
            # 'alerta':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte propósito.', 'style': 'margin-top:10px'})

        }
