from django import forms
from django.forms.widgets import TimeInput, DateInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Registro


class RegistroGeneralForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['Canasta', 'Fecha']
        widgets = {
            'Fecha': DateInput(attrs={'type': 'date'})
        }

class RegistroCanastaForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['Contenido_Total', 'Azucar', 'Sorbato', 'Producto_no_Conforme', 'Fruta_Seleccionada']

class RegistroTiemposForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['Inicio', 'Primera_Coccion', 'Enfriamiento', 'Despulpado',
                  'Segunda_Coccion', 'Empaque', 'Hora_Final']
        widgets = {
            'Inicio': TimeInput(attrs={'type': 'time'}),
            'Primera_Coccion': TimeInput(attrs={'type': 'time'}),
            'Enfriamiento': TimeInput(attrs={'type': 'time'}),
            'Despulpado': TimeInput(attrs={'type': 'time'}),
            'Segunda_Coccion': TimeInput(attrs={'type': 'time'}),
            'Empaque': TimeInput(attrs={'type': 'time'}),
            'Hora_Final' : TimeInput(attrs={'type': 'time'}),
        }

class RegistroDesechosForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['Semilla', 'Pulpa']

class RegistroBrixForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['Valor_Primer_Brix', 'Hora_Primer_Brix', 'Valor_Brix_Final', 'Hora_Brix_Final']
        widgets = {
            'Hora_Primer_Brix': TimeInput(attrs={'type': 'time'}),
            'Hora_Brix_Final': TimeInput(attrs={'type': 'time'}),
        }

class RegistroEmpacadosForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['Producto_Terminado', 'Media_Libra', 'Libra', 'Bolsa_Cinco_kg', 'Otro']


class SeleccionarRegistrosForm(forms.Form):
    registros = forms.ModelMultipleChoiceField(queryset=Registro.objects.all())

class CompararRegistrosForm(forms.Form):
    registros = forms.ModelMultipleChoiceField(
        queryset=Registro.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

class RegistrodeUsuarioForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma tu Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        

