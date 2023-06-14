# Generated by Django 4.1.5 on 2023-06-11 17:08

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(regex='\\D*\\(?(\\d{3})?\\)?\\D*(\\d{4})\\D*(\\d{4})')], verbose_name='Telefono del usuario')),
                ('cantlibrosPrestados', models.IntegerField(verbose_name='Cantidad de Libros Prestados Actualmente')),
                ('tipoTrabajo', models.CharField(choices=[('Docente', 'Docente'), ('Estudiante', 'Estudiante'), ('Trabajador', 'Trabajador')], max_length=50, verbose_name='Tipo de Trabajo')),
                ('nivelMorosidad', models.CharField(choices=[('Ninguno', 'Ninguno'), ('Morosa tipo A', 'Morosa tipo A'), ('Morosa tipo B', 'Morosa tipo B'), ('Morosa tipo C', 'Morosa tipo C')], max_length=50, verbose_name='Nivel de Morosidad')),
                ('cantidadMoraPagar', models.FloatField(default='0.00', verbose_name='Cantidad en dolares a pagar por mora')),
                ('user', models.OneToOneField(limit_choices_to={'is_superuser': False}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'db_table': 'Persona',
                'ordering': ['id'],
            },
        ),
    ]