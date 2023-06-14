# Generated by Django 4.1.5 on 2023-06-11 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paisCodigo', models.CharField(max_length=3, verbose_name='Codigo del Pais')),
                ('paisNombre', models.CharField(max_length=52, verbose_name='Nombre de Pais')),
                ('paisContinente', models.CharField(default='Asia', max_length=50, verbose_name='Continente del Pais')),
                ('paisRegion', models.CharField(max_length=26, verbose_name='Región del Pais')),
                ('paisArea', models.FloatField(default='0.00', verbose_name='Area del Pais')),
                ('paisIndependencia', models.SmallIntegerField(null=True, verbose_name='Independencia del Pais')),
                ('paisPoblacion', models.IntegerField(verbose_name='Poblacion del Pais')),
                ('paisExpectativaDeVida', models.FloatField(null=True, verbose_name='Expectativa de Vida del Pais')),
                ('paisProductoInternoBruto', models.FloatField(null=True, verbose_name='Producto Interno Bruto del Pais')),
                ('PaisProductoInternoBrutoAntiguo', models.FloatField(null=True, verbose_name='Producto Interno Bruto Antiguo del Pais')),
                ('paisNombreLocal', models.CharField(max_length=45, verbose_name='Nombre Local del Pais')),
                ('paisGobierno', models.CharField(max_length=45, verbose_name='Gobierno del Pais')),
                ('paisJefeDeEstado', models.CharField(max_length=60, null=True, verbose_name='Jefe de Estado del Pais')),
                ('paisCapital', models.IntegerField(null=True, verbose_name='Capital del Pais')),
                ('paisCodigo2', models.CharField(max_length=3, verbose_name='Segundo Codigo del Pais')),
            ],
            options={
                'verbose_name': 'Pais',
                'verbose_name_plural': 'Paises',
                'db_table': 'Pais',
                'ordering': ['paisNombre'],
            },
        ),
    ]
