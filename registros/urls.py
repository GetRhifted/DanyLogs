from django.urls import path
from . import views 

app_name = 'registros'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('registro_wizard/', views.RegistroWizardView.as_view(), name='registro_wizard'),
    path('registro_completado/', views.RegistroCompletadoView.as_view(), name='registro_completado'),
    path('registro_detallado/<int:pk>/', views.RegistroDetalladoView.as_view(), name='registro_detallado'),
    path('edicion_registro/<int:pk>/', views.RegistroUpdateView.as_view(), name='edicion_registro'),
    path('edicion_registro2/<int:pk>/', views.RegistroUpdateView2.as_view(), name='edicion_registro2'),
    path('edicion_registro3/<int:pk>/', views.RegistroUpdateView3.as_view(), name='edicion_registro3'),
    path('edicion_registro4/<int:pk>/', views.RegistroUpdateView4.as_view(), name='edicion_registro4'),
    path('edicion_registro5/<int:pk>/', views.RegistroUpdateView5.as_view(), name='edicion_registro5'),
    path('edicion_registro6/<int:pk>/', views.RegistroUpdateView6.as_view(), name='edicion_registro6'),
]