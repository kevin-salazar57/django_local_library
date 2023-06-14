from django.contrib import admin
from apps.estado import models
# Register your models here.
admin.site.site_header = 'Desa System'
admin.site.index_title = 'Sistema de Gestión Bibliotecario'
admin.site.site_title = 'Desa System'
admin.site.register(models.Estado)
