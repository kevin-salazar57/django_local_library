from django.contrib import admin
from apps.recurso import models
from django.contrib import messages

# Register your models here.
@admin.action(permissions=["change"])
@admin.action(description='Marcar Libro como Prestado')
def actualizar_Estado_Prestado(modeladmin, request, queryset):
    queryset.update(estado = 2 )
    messages.success(request, "El estado del Libro se ha actualizado a Prestado exitosamente")

@admin.action(permissions=["change"])
@admin.action(description='Marcar Libro como Disponible')
def actualizar_Estado_Disponible(modeladmin, request, queryset):
    queryset.update(estado = 1 )
    messages.success(request, "El estado del Libro se ha actualizado a Disponible exitosamente")

class RecursoAdmin(admin.ModelAdmin):
    list_display = ('name','editorial','aniopublicacion','volumen','codigoInterno','estado')
    search_fields = ('name','codigoInterno')
    list_filter = ['estado']
    actions = [actualizar_Estado_Prestado, actualizar_Estado_Disponible]

admin.site.site_header = 'Desa System'
admin.site.index_title = 'Sistema de Gestión Bibliotecario'
admin.site.site_title = 'Desa System'
admin.site.register(models.Recurso, RecursoAdmin)