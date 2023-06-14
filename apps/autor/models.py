from django.db import models
from apps.pais.models import Pais

# Create your models here.
#Clase Autor
class Autor(models.Model):
     name = models.CharField(max_length=150, verbose_name='Nombre del Autor', unique=True)
     apellido = models.CharField(max_length=150, verbose_name ='Apellido del Autor')
     nacionalidad = models.ManyToManyField(Pais, verbose_name='Pais de Nacimiento',related_name='autorNacionalidad')
     fechaNacimiento = models.DateTimeField(verbose_name='Fecha de Nacimiento')


     def __str__(self):
          return 'Nombre del autor: {} {}'.format(self.name, self.apellido)

     class Meta:
          verbose_name = 'Autor'
          verbose_name_plural = 'Autores'
          db_table = 'Autor'
          ordering = ['id']