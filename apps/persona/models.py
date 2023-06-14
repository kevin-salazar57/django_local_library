from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Create your models here.
#Clase Persona
class Persona(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'is_superuser': False})
    numTelefonoRegex = RegexValidator(regex = '\D*\(?(\d{3})?\)?\D*(\d{4})\D*(\d{4})')
    telefono = models.CharField(verbose_name='Telefono del usuario',validators = [numTelefonoRegex], max_length = 8)
    cantlibrosPrestados = models.IntegerField(verbose_name='Cantidad de Libros Prestados Actualmente')
    clasePersona = [
        ("Docente", "Docente"),
        ("Estudiante", "Estudiante"),
        ("Trabajador", "Trabajador"),
    ]
    tipoTrabajo =models.CharField(max_length=50, verbose_name='Tipo de Trabajo', choices=clasePersona)
    tipoPersona = [
        ("Ninguno","Ninguno"),
        ("Morosa tipo A", "Morosa tipo A"),
        ("Morosa tipo B", "Morosa tipo B"),
        ("Morosa tipo C", "Morosa tipo C"),
    ]
    nivelMorosidad = models.CharField(max_length=50, verbose_name='Nivel de Morosidad',choices=tipoPersona)
    cantidadMoraPagar = models.FloatField(verbose_name='Cantidad en dolares a pagar por mora', default="0.00") 
    
    def __str__(self):
        return format(self.user)
    
    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        db_table = 'Persona'
        ordering = ['id']