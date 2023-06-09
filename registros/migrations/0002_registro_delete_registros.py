# Generated by Django 4.2.1 on 2023-05-07 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bache', models.CharField(max_length=20)),
                ('Fecha', models.DateField()),
                ('Gramos_de_Mora', models.FloatField(default=0.0)),
                ('Gramos_de_Azucar', models.FloatField(default=0.0)),
                ('Gramos_de_Sorbato', models.FloatField(default=0.0)),
                ('Hora_Inicio', models.TimeField()),
                ('Primer_Hervor', models.TimeField()),
                ('Pausa_de_enfriado', models.TimeField()),
                ('Despulpado', models.TimeField()),
                ('Ultima_Coccion', models.TimeField()),
                ('Hora_Final', models.TimeField()),
                ('Desechos_Mora', models.FloatField(default=0.0)),
                ('Semilla', models.FloatField(default=0.0)),
                ('Pulpa', models.FloatField(default=0.0)),
                ('Valor_Primer_Brix', models.FloatField(default=0.0)),
                ('Hora_Primer_Brix', models.TimeField()),
                ('Valor_Brix_Final', models.FloatField(default=0.0)),
                ('Hora_Brix_Final', models.TimeField()),
                ('Paquete_250_gr', models.IntegerField(default=0)),
                ('Paquete_500_gr', models.IntegerField(default=0)),
                ('Paquete_5000_gr', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Registros',
        ),
    ]
