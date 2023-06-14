from django.contrib import admin
from apps.persona import models
from django.db.models import F, IntegerField, ExpressionWrapper
from django.contrib import messages

# Register your models here.
@admin.action(permissions=["change"])
@admin.action(description='Validez para prestamo')
def apta_Prestamo(modeladmin, request, queryset):
    cantLibros_Prestado = F("cantlibrosPrestados")
    cantLibros_Prestado_int = queryset.annotate(int_value=ExpressionWrapper(cantLibros_Prestado, output_field=IntegerField())).values('int_value')
    valor_entero = cantLibros_Prestado_int[0]['int_value']
    if valor_entero < 5 :
        messages.success(request, "Persona Apta para la realización de prestamo")
    elif valor_entero >= 5:
        messages.error(request, "Persona No Apta para la realización de prestamo, Supera la política del máximo de libros prestados por persona")

@admin.action(permissions=["change"])
@admin.action(description='Aumento de cantidad de Libros Prestados')
def realizar_Prestamo(modeladmin, request, queryset):
    cantLibros_Prestado = F("cantlibrosPrestados")
    cantLibros_Prestado_int = queryset.annotate(int_value=ExpressionWrapper(cantLibros_Prestado, output_field=IntegerField())).values('int_value')
    valor_entero = cantLibros_Prestado_int[0]['int_value']
    if valor_entero <5 :
        queryset.update(cantlibrosPrestados = F("cantlibrosPrestados")+1 )
        messages.success(request, "Aumento de cantidad de libros prestada exitosa")
    elif valor_entero >=5 :
        messages.error(request, "Supera la política del máximo de libros prestados por persona")

@admin.action(permissions=["change"])
@admin.action(description='Disminución de cantidad de Libros Prestados')
def devolución_Prestamo(modeladmin, request, queryset):
    cantLibros_Prestado = F("cantlibrosPrestados")
    cantLibros_Prestado_int = queryset.annotate(int_value=ExpressionWrapper(cantLibros_Prestado, output_field=IntegerField())).values('int_value')
    valor_entero = cantLibros_Prestado_int[0]['int_value']
    if valor_entero > 0 :
        queryset.update(cantlibrosPrestados = F("cantlibrosPrestados")-1 )
        messages.success(request, "Disminución de cantidad de libros prestada exitosa")
    elif valor_entero <=0 :
        messages.error(request, "No posee recursos que deba devolver")

@admin.action(permissions=["change"])
@admin.action(description='Asignar Mora por valor de libro')
def asignar_Mora(modeladmin, request, queryset):
    queryset.update(cantidadMoraPagar =  F("cantidadMoraPagar")+10.00 )
    messages.success(request, "La mora de $10 ha sido asignada exitosamente")

@admin.action(permissions=["change"])
@admin.action(description='Asignar Mora por día retrasado')
def asignar_Mora_Dia(modeladmin, request, queryset):
    queryset.update(cantidadMoraPagar =  F("cantidadMoraPagar")+1.00 )
    messages.success(request, "La mora de $10 ha sido asignada exitosamente")

@admin.action(permissions=["change"])
@admin.action(description='Liberar de Mora de precio de libro ')
def pagar_Mora(modeladmin, request, queryset):
    cantLibros_Prestado = F("cantidadMoraPagar")
    cantLibros_Prestado_int = queryset.annotate(int_value=ExpressionWrapper(cantLibros_Prestado, output_field=IntegerField())).values('int_value')
    valor_entero = cantLibros_Prestado_int[0]['int_value']
    if valor_entero > 0 :
        queryset.update(cantidadMoraPagar =  F("cantidadMoraPagar")-10.00 )
        messages.success(request, "La mora de $10 ha sido deducida exitosamente")
    elif valor_entero <=0 :
        messages.error(request, "No posee Mora que deba pagar")


@admin.action(permissions=["change"])
@admin.action(description='Liberar de Mora por día retrasado')
def pagar_Mora_Dia(modeladmin, request, queryset):
    cantLibros_Prestado = F("cantidadMoraPagar")
    cantLibros_Prestado_int = queryset.annotate(int_value=ExpressionWrapper(cantLibros_Prestado, output_field=IntegerField())).values('int_value')
    valor_entero = cantLibros_Prestado_int[0]['int_value']
    if valor_entero > 0 :
        queryset.update(cantidadMoraPagar =  F("cantidadMoraPagar")-1.00 )
        messages.success(request, "La mora de $1 ha sido deducida exitosamente")
    elif valor_entero <=0 :
        messages.error(request, "No posee Mora que deba pagar")

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('user','telefono','cantlibrosPrestados','tipoTrabajo','nivelMorosidad','cantidadMoraPagar')
    search_fields = ('telefono','nivelMorosidad')
    list_filter = ["nivelMorosidad"]
    actions = [apta_Prestamo, realizar_Prestamo, devolución_Prestamo, asignar_Mora, asignar_Mora_Dia, pagar_Mora, pagar_Mora_Dia]
    

admin.site.site_header = 'Desa System'
admin.site.index_title = 'Sistema de Gestión Bibliotecario'
admin.site.site_title = 'Desa System'
admin.site.register(models.Persona, PersonaAdmin)
