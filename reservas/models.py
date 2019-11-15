from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Ciudad (models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
       return self.nombre

    class Meta : 
        verbose_name_plural = "Ciudades"

class Propiedad (models.Model):
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='images', default = 'images/bg.jpg')
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio_diario = models.FloatField(null=False, default=0.00)
    max_pax = models.IntegerField(null=False)
    dueño = models.ForeignKey(User, null=False, blank=False, on_delete=models.DO_NOTHING)
    
    def __unicode__(self):
        return self.titulo

    class Meta : 
        verbose_name_plural = "Propiedades"

class Reserva(models.Model):
    fecha_reserva = models.DateField(auto_now_add=True)
    codigo = models.CharField(max_length=100, null=False, blank=False)
    total = models.FloatField(null=True, default=None)
    class Meta : 
        verbose_name_plural = "Reservas"

class Fecha_Alquiler(models.Model):
    propiedad = models.ForeignKey(Propiedad, null=False, blank=False, on_delete=models.DO_NOTHING)
    reserva = models.ForeignKey(Reserva, null=True, blank=True, on_delete=models.DO_NOTHING)
    fecha_alq = models.DateField(null=False)
    class Meta : 
        verbose_name_plural = "Fechas Alquileres"



