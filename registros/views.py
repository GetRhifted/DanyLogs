from django.shortcuts import render, redirect
from .forms import RegistroGeneralForm, RegistroIngredientesForm, RegistroTiemposForm, RegistroDesechosForm, RegistroBrixForm, RegistroPaquetesForm
from formtools.wizard.views import SessionWizardView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView, DetailView, UpdateView
from. models import Registro

class HomeView(ListView):
    model = Registro
    template_name = 'registros/home.html'
    queryset = Registro.objects.order_by('-id')[:10]

class RegistroWizardView(SessionWizardView):
    template_name = 'registros/registro_wizard.html'
    form_list = [RegistroGeneralForm, RegistroIngredientesForm, RegistroTiemposForm, RegistroDesechosForm,
                 RegistroBrixForm, RegistroPaquetesForm]
    #success_url = reverse_lazy('registros:registro_completado')

    def done(self, form_list, **kwargs):
        registro = Registro(Bache=form_list[0].cleaned_data['Bache'],
                            Fecha=form_list[0].cleaned_data['Fecha'],
                            Gramos_de_Mora=form_list[1].cleaned_data['Gramos_de_Mora'],
                            Gramos_de_Azucar=form_list[1].cleaned_data['Gramos_de_Azucar'],
                            Gramos_de_Sorbato=form_list[1].cleaned_data['Gramos_de_Sorbato'],
                            Hora_Inicio=form_list[2].cleaned_data['Hora_Inicio'],
                            Primer_Hervor=form_list[2].cleaned_data['Primer_Hervor'],
                            Pausa_de_enfriado=form_list[2].cleaned_data['Pausa_de_enfriado'],
                            Despulpado=form_list[2].cleaned_data['Despulpado'],
                            Ultima_Coccion=form_list[2].cleaned_data['Ultima_Coccion'],
                            Hora_Final=form_list[2].cleaned_data['Hora_Final'],
                            Desechos_Mora=form_list[3].cleaned_data['Desechos_Mora'],
                            Semilla=form_list[3].cleaned_data['Semilla'],
                            Pulpa=form_list[3].cleaned_data['Pulpa'],
                            Valor_Primer_Brix=form_list[4].cleaned_data['Valor_Primer_Brix'],
                            Hora_Primer_Brix=form_list[4].cleaned_data['Hora_Primer_Brix'],
                            Valor_Brix_Final=form_list[4].cleaned_data['Valor_Brix_Final'],
                            Hora_Brix_Final=form_list[4].cleaned_data['Hora_Brix_Final'],
                            Paquete_250_gr=form_list[5].cleaned_data['Paquete_250_gr'],
                            Paquete_500_gr=form_list[5].cleaned_data['Paquete_500_gr'],
                            Paquete_5000_gr=form_list[5].cleaned_data['Paquete_5000_gr'],
                            )
        registro.save()
        return redirect('registros:registro_completado')
    
    def get_success_url(self):
        return reverse('registros:registro_completado')
        
class RegistroCompletadoView(TemplateView):
    model = Registro
    form_class = RegistroGeneralForm
    template_name = 'registros/registro_completado.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['registro'] = Registro.objects.last()
        return context

    def form_valid(self, form):
        # Guarda el registro y asigna la instancia del objeto a la variable 'registro'
        registro = form.save()
        # Agrega el objeto de registro al contexto de la plantilla
        return render(self.request, self.template_name, {'registro': registro})
    
class RegistroDetalladoView(DetailView):
    model = Registro
    template_name = 'registros/registro_detallado.html'

class RegistroUpdateView(UpdateView):
     model = Registro
     form_class = RegistroGeneralForm
     template_name = 'registros/edicion_registro.html'
     
     def get_success_url(self):
        return reverse_lazy('registros:edicion_registro2', kwargs={'pk': self.object.pk})

class RegistroUpdateView2(UpdateView):
     model = Registro
     form_class = RegistroIngredientesForm
     template_name = 'registros/edicion_registro2.html'
     
     def get_success_url(self):
        return reverse_lazy('registros:edicion_registro3', kwargs={'pk': self.object.pk})

class RegistroUpdateView3(UpdateView):
     model = Registro
     form_class = RegistroTiemposForm
     template_name = 'registros/edicion_registro3.html'
     
     def get_success_url(self):
        return reverse_lazy('registros:edicion_registro4', kwargs={'pk': self.object.pk})

class RegistroUpdateView4(UpdateView):
     model = Registro
     form_class = RegistroDesechosForm
     template_name = 'registros/edicion_registro4.html'
     
     def get_success_url(self):
        return reverse_lazy('registros:edicion_registro5', kwargs={'pk': self.object.pk})

class RegistroUpdateView5(UpdateView):
     model = Registro
     form_class = RegistroBrixForm
     template_name = 'registros/edicion_registro5.html'
     
     def get_success_url(self):
        return reverse_lazy('registros:edicion_registro6', kwargs={'pk': self.object.pk})

class RegistroUpdateView6(UpdateView):
     model = Registro
     form_class = RegistroPaquetesForm
     template_name = 'registros/edicion_registro6.html'
     
     def get_success_url(self):
        return reverse_lazy('registros:registro_detallado', kwargs={'pk': self.object.pk})




