from django.db import models

# Create your models here.
#Clase Estado
class Estado(models.Model):
     name = models.CharField(max_length=150, verbose_name='Estado del Libro', unique=True)

     def __str__(self):
          return self.name

     class Meta:
          verbose_name = 'Estado'
          verbose_name_plural = 'Estados'
          db_table = 'Estado'
          ordering = ['id']