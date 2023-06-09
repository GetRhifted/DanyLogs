from django import forms
from django.forms.widgets import TimeInput, DateInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Registro


class RegistroGeneralForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['Bache', 'Fecha']
        widgets = {
            'Fecha': DateInput(attrs={'type': 'date'})
        }

class RegistroIngredientesForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['Gramos_de_Mora', 'Gramos_de_Azucar', 'Gramos_de_Sorbato']

class RegistroTiemposForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['Hora_Inicio', 'Primer_Hervor', 'Pausa_de_enfriado', 'Despulpado',
                  'Ultima_Coccion', 'Hora_Final']
        widgets = {
            'Hora_Inicio': TimeInput(attrs={'type': 'time'}),
            'Primer_Hervor': TimeInput(attrs={'type': 'time'}),
            'Pausa_de_enfriado': TimeInput(attrs={'type': 'time'}),
            'Despulpado': TimeInput(attrs={'type': 'time'}),
            'Ultima_Coccion': TimeInput(attrs={'type': 'time'}),
            'Hora_Final': TimeInput(attrs={'type': 'time'}),
        }

class RegistroDesechosForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['Desechos_Mora', 'Semilla', 'Pulpa']

class RegistroBrixForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['Valor_Primer_Brix', 'Hora_Primer_Brix', 'Valor_Brix_Final', 'Hora_Brix_Final']
        widgets = {
            'Hora_Primer_Brix': TimeInput(attrs={'type': 'time'}),
            'Hora_Brix_Final': TimeInput(attrs={'type': 'time'}),
        }

class RegistroPaquetesForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['Paquete_250_gr', 'Paquete_500_gr', 'Paquete_5000_gr']


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
        

