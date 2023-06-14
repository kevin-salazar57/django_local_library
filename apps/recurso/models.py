from django.db import models
from apps.categoria.models import Categoria
from apps.autor.models import Autor
from apps.estado.models import Estado

# Create your models here.

#Clase Recurso
class Recurso(models.Model):
     name = models.CharField(max_length=200, verbose_name='Nombre de Recurso')
     categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
     autor = models.ManyToManyField(Autor, related_name='autorRecurso')
     editorial = models.CharField(max_length=200, verbose_name='Editorial del Recurso',default='')
     aniopublicacion = models.IntegerField(verbose_name='Año de Publicación',  default='0') 
     volumen = models.IntegerField(verbose_name='Numero de Volumen', default='0')
     codigoInterno = models.IntegerField(verbose_name='Codigo de Biblioteca', default='0')
     cantidad = models.IntegerField(default='0')
     estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

     def __str__(self):
          return self.name             

     class Meta:
          verbose_name = 'Recurso'
          verbose_name_plural = 'Recursos'
          db_table = 'Recurso'
          ordering = ['id']