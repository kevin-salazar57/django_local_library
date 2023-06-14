from django.db import models

# Create your models here.

#Clase Categoria
class Categoria(models.Model):
     name = models.CharField(max_length=150, verbose_name='Nombre de Categoria', unique=True)

     def __str__(self):
          return self.name

     class Meta:
          verbose_name = 'Categoria'
          verbose_name_plural = 'Categorias'
          db_table = 'categoria'
          ordering = ['id']