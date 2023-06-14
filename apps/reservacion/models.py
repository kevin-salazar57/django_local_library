from django.db import models
from apps.recurso.models import Recurso
from apps.persona.models import Persona
# Create your models here.
class Reservacion(models.Model):
#Aqui se agregaran los demás atributos de la tabla que aparecera en la base de datos como columnas
    user  = models.OneToOneField(Persona, on_delete=models.CASCADE,verbose_name='Nombre de Usuario que quiere reservar')
    libroReservado = models.ForeignKey(Recurso, on_delete=models.CASCADE,verbose_name='Libro a Reservar',limit_choices_to={'estado': 2})
    fechaReservación = models.DateField(verbose_name='Fecha de reservación del recurso')  
    estados = [
        ("Activo", "Activo"),
        ("Cancelado", "Cancelado"),
    ]
    estadoReservacion = models.CharField(max_length=9, verbose_name='Estado de la Reservación', choices=estados)

    def __str__(self):
        return 'Usuario que hizo la reservación: {}, Libro reservado: {}'.format(self.user, self.libroReservado)

    class Meta:
        verbose_name = 'Reservación'
        verbose_name_plural = 'Reservaciones'
        db_table = 'Reservacion'
        ordering = ['id']
