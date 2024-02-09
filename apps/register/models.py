from django.db import models
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import F
from django.db.models import ImageField
# Create your models here.

class SeleccionadoDeportivo (models.Model):
    name=models.CharField(max_length=255,verbose_name='Nombre')
    rama=models.CharField(max_length=255,verbose_name='rama')
    def __str__(self):
        return f'{self.name} - {self.rama}'
    
    class Meta:
        verbose_name='SeleccionadoDeportivo'
        verbose_name_plural='SeleccionadosDeportivos'
        db_table='SeleccionadoDeportivo'
        ordering=['id']
        
class Estamento (models.Model):
    name=models.CharField(max_length=150,verbose_name='Nombre')
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name='estamento'
        verbose_name_plural='estamentos'
        db_table='estamento'
        ordering=['id']   
        
class Deportistas(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre', blank=False)
    apellidos = models.CharField(max_length=255, verbose_name='Apellidos', blank=False)
    cedula = models.CharField(max_length=255,unique=True, verbose_name='Cedula', blank=False)
    codigo = models.CharField(max_length=255,unique=True, verbose_name='Codigo', blank=False)
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento', blank=False)
    edad = models.IntegerField(verbose_name='Edad')
    genero = models.CharField(max_length=255, verbose_name='Genero', blank=False)
    altura = models.FloatField(verbose_name='Altura', blank=False, validators=[MinValueValidator(0), MaxValueValidator(3)])
    peso = models.FloatField(verbose_name='Peso', blank=False, validators=[MinValueValidator(0), MaxValueValidator(200)])
    talla_camisa = models.CharField(max_length=255, verbose_name='Talla de Camisa', blank=False)
    talla_pantalon = models.CharField(max_length=255, verbose_name='Talla de Pantalon', blank=False)
    fecha_vinculacion = models.DateField(verbose_name='Fecha de Vinculacion', blank=False)
    Estamento = models.ForeignKey(Estamento, on_delete=models.PROTECT, verbose_name='Estamento', blank=False)
    SeleccionadoDeportivo = models.ForeignKey(SeleccionadoDeportivo, on_delete=models.PROTECT, verbose_name='Seleccionado Deportivo', blank=False)
    promedio_total_acomulado = models.FloatField(verbose_name='Promedio Total Acomulado', blank=False, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.nombre} - {self.apellidos} '
    class Meta:
        verbose_name = 'Deportista'
        verbose_name_plural = 'Deportistas'
        db_table = 'Deportistas'
        ordering = ['id']
class Asistencia(models.Model):

    # Definir los atributos de la clase
    deportista = models.ForeignKey(Deportistas, on_delete=models.PROTECT, verbose_name='Deportista', limit_choices_to={'SeleccionadoDeportivo': F('seleccionado_deportivo')})
    seleccionado_deportivo = models.ForeignKey(SeleccionadoDeportivo, on_delete=models.PROTECT, verbose_name='Seleccionado Deportivo')
    fecha = models.DateField(verbose_name='Fecha')
    hora = models.TimeField(verbose_name='Hora')

    def __str__(self) -> str:

        return f'{self.deportista} - {self.seleccionado_deportivo} - {self.fecha} - {self.hora}'

    class Meta:

        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'
        db_table = 'Asistencia'
        ordering = ['fecha', 'hora']