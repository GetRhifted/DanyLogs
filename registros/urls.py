from django.urls import path
from . import views 

app_name = 'registros'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('registro_wizard/', views.RegistroWizardView.as_view(), name='registro_wizard'),
    path('registro_completado/', views.RegistroCompletadoView.as_view(), name='registro_completado'),
    path('registro_detallado/<int:pk>/', views.RegistroDetalladoView.as_view(), name='registro_detallado'),
]