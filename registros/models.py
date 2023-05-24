from django.db import models
from django.contrib.auth.models import User

class Registro(models.Model):    
    Canasta = models.CharField(max_length=100)
    Fecha = models.DateField()

    Contenido_Total = models.FloatField(default=0.0)
    Azucar = models.FloatField(default=0.0)
    Sorbato = models.FloatField(default=0.0)
    Producto_no_Conforme = models.FloatField(default=0.0)
    Fruta_Seleccionada = models.FloatField(default=0.0)
    
    Inicio = models.TimeField()
    Primera_Coccion = models.TimeField()
    Enfriamiento = models.TimeField()
    Despulpado = models.TimeField()
    Segunda_Coccion = models.TimeField()
    Empaque = models.TimeField()
    Hora_Final = models.TimeField()

    Semilla = models.FloatField(default=0.0)
    Pulpa = models.FloatField(default=0.0)

    Valor_Primer_Brix = models.FloatField(default=0.0)
    Hora_Primer_Brix = models.TimeField()
    Valor_Brix_Final = models.FloatField(default=0.0)
    Hora_Brix_Final = models.TimeField()

    Producto_Terminado = models.IntegerField(default=0) 
    Media_Libra = models.IntegerField(default=0)
    Libra = models.IntegerField(default=0)
    Bolsa_Cinco_kg = models.IntegerField(default=0)
    Otro = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.Canasta


