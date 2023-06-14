from django.db import models
from apps.recurso.models import Recurso
from apps.persona.models import Persona
# Create your models here.
#Clase Prestamo
class Prestamo(models.Model):
    #Aqui se agregaran los demás atributos de la tabla que aparecera en la base de datos como columnas
    user  = models.ForeignKey(Persona, on_delete=models.CASCADE,verbose_name='Nombre de Usuario')
    libroPrestado = models.ForeignKey(Recurso, on_delete=models.CASCADE,verbose_name='Libro Prestado', limit_choices_to={'estado': 1})
    fechaInicioPrestamo = models.DateField(verbose_name='Fecha de incio que se realizó el prestamo')
    fechaFinPrestamo = models.DateField(verbose_name='Fecha de devolución del prestamo')
    fechaRealPrestamo = models.DateField(verbose_name='Fecha real que se devolvió el prestamo',  blank=True, null=True)    
    estados = [
        ("Activo", "Activo"),
        ("Devuelto", "Devuelto"),
        ("Atrasado", "Atrasado"),
    ]
    estadoPrestamo = models.CharField(max_length=8, verbose_name='Estado del Prestamo', choices=estados)
    choicesEntregaRecurso = [
        ("Pendiente de entregar","Pendiente de entregar"),
        ("Entregado","Entregado")
    ]
    entregaRecurso = models.CharField(max_length=21, verbose_name='Estado de entrega de recurso', choices=choicesEntregaRecurso, default='Pendiente de entregar')
    fechaEntregaRecurso = models.DateField(verbose_name='Fecha en que se entrego el recurso',  blank=True, null=True) 

    def __str__(self):
        return 'Usuario que hizo el prestamo: {}, Libro Prestado: {}'.format(self.user, self.libroPrestado)
    
    def get_cantLibros(self, obj, request):
        return format(self.user.cantlibrosPrestados)
    
    class Meta:
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'
        db_table = 'Prestamo'
        ordering = ['id']
