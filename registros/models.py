from django.db import models
import datetime

class Registro(models.Model):
    Bache = models.CharField(max_length=100)
    Fecha = models.DateField()

    Gramos_de_Mora = models.FloatField(default=0.0)
    Gramos_de_Azucar = models.FloatField(default=0.0)
    Gramos_de_Sorbato = models.FloatField(default=0.0)

    Hora_Inicio = models.TimeField()
    Primer_Hervor = models.TimeField()
    Pausa_de_enfriado = models.TimeField()
    Despulpado = models.TimeField()
    Ultima_Coccion = models.TimeField()
    Hora_Final = models.TimeField()

    Desechos_Mora = models.FloatField(default=0.0)
    Semilla = models.FloatField(default=0.0)
    Pulpa = models.FloatField(default=0.0)

    Valor_Primer_Brix = models.FloatField(default=0.0)
    Hora_Primer_Brix = models.TimeField()
    Valor_Brix_Final = models.FloatField(default=0.0)
    Hora_Brix_Final = models.TimeField()

    Paquete_250_gr = models.IntegerField(default=0)
    Paquete_500_gr = models.IntegerField(default=0)
    Paquete_5000_gr = models.IntegerField(default=0)

    def __str__(self):
        return self.Bache


