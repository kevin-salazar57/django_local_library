from django.db import models

# Create your models here.
#Clase pais
class Pais(models.Model):
    paisCodigo = models.CharField(max_length=3,verbose_name='Codigo del Pais')
    paisNombre = models.CharField(max_length=52, verbose_name='Nombre de Pais')
    paisContinente = models.CharField(max_length=50, verbose_name='Continente del Pais', default='Asia')
    paisRegion = models.CharField(max_length=26, verbose_name='Región del Pais')
    paisArea = models.FloatField(verbose_name='Area del Pais', default='0.00')
    paisIndependencia= models.SmallIntegerField(verbose_name='Independencia del Pais', null=True)
    paisPoblacion = models.IntegerField(verbose_name='Poblacion del Pais')
    paisExpectativaDeVida = models.FloatField(verbose_name='Expectativa de Vida del Pais', null=True)
    paisProductoInternoBruto = models.FloatField(verbose_name='Producto Interno Bruto del Pais', null=True)
    PaisProductoInternoBrutoAntiguo = models.FloatField(verbose_name='Producto Interno Bruto Antiguo del Pais', null=True)
    paisNombreLocal = models.CharField(max_length=45,verbose_name='Nombre Local del Pais') # varchar(45) NOT NULL DEFAULT '',
    paisGobierno = models.CharField(max_length=45,verbose_name='Gobierno del Pais') #varchar(45) NOT NULL DEFAULT '',
    paisJefeDeEstado = models.CharField(max_length=60,verbose_name='Jefe de Estado del Pais', null=True) #varchar(60) DEFAULT NULL,
    paisCapital= models.IntegerField(verbose_name='Capital del Pais', null=True) #int DEFAULT NULL,
    paisCodigo2 = models.CharField(max_length=3,verbose_name='Segundo Codigo del Pais') #char(2) NOT NULL DEFAULT '',

    def __str__(self):
        return self.paisNombre

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
        db_table = 'Pais'
        ordering = ['paisNombre']