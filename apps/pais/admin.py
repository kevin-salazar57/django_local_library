from django.contrib import admin
from apps.pais import models
# Register your models here.
class PaisAdmin(admin.ModelAdmin):
    list_display = ('paisCodigo','paisNombre','paisContinente','paisCodigo2')
    search_fields = ('paisCodigo','paisNombre','paisCodigo2')

admin.site.site_header = 'Desa System'
admin.site.index_title = 'Sistema de Gestión Bibliotecario'
admin.site.site_title = 'Desa System'
admin.site.register(models.Pais,PaisAdmin)
