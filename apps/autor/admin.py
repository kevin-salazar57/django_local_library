from django.contrib import admin
from apps.autor import models
# Register your models here.
class AutorAdmin(admin.ModelAdmin):
    list_display = ('name','apellido','fechaNacimiento')
    search_fields = ('name','apellido')

admin.site.site_header = 'Desa System'
admin.site.index_title = 'Sistema de Gestión Bibliotecario'
admin.site.site_title = 'Desa System'

admin.site.register(models.Autor, AutorAdmin)