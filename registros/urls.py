from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

from . import views 

app_name = 'registros'

urlpatterns = [
    path('', login_required(views.HomeView.as_view()), name='home'),
    path('registro_wizard/', login_required(views.RegistroWizardView.as_view()), name='registro_wizard'),
    path('registro_completado/', login_required(views.RegistroCompletadoView.as_view()), name='registro_completado'),
    path('registro_detallado/<int:pk>/', login_required(views.RegistroDetalladoView.as_view()), name='registro_detallado'),
    path('edicion_registro/<int:pk>/', login_required(views.RegistroUpdateView.as_view()), name='edicion_registro'),
    path('edicion_registro2/<int:pk>/', login_required(views.RegistroUpdateView2.as_view()), name='edicion_registro2'),
    path('edicion_registro3/<int:pk>/', login_required(views.RegistroUpdateView3.as_view()), name='edicion_registro3'),
    path('edicion_registro4/<int:pk>/', login_required(views.RegistroUpdateView4.as_view()), name='edicion_registro4'),
    path('edicion_registro5/<int:pk>/', login_required(views.RegistroUpdateView5.as_view()), name='edicion_registro5'),
    path('edicion_registro6/<int:pk>/', login_required(views.RegistroUpdateView6.as_view()), name='edicion_registro6'),
    path('comparar_registros/', login_required(views.CompararRegistrosView.as_view()), name='comparar_registros'),
    path('borrar_registro/<int:pk>/', login_required(views.RegistroDeleteView.as_view()), name='borrar_registro'),
    path('busqueda/', login_required(views.BuscarRegistroView.as_view()), name='busqueda'),
    path('registro_usuario/', views.RegistroUsuarioView.as_view(), name='registro_usuario'),
    path('login/', LoginView.as_view(template_name='registros/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]