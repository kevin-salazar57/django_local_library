from django.contrib import admin
from apps.reservacion import models
from django.db.models import F, IntegerField, CharField, ExpressionWrapper
from django.contrib import messages

# Register your models here.
@admin.action(permissions=["change"])
@admin.action(description='Cancelar Reservación')
def cancelar_Reservacion(modeladmin, request, queryset):
    cantLibros_Prestado = F("estadoReservacion")
    cantLibros_Prestado_int = queryset.annotate(int_value=ExpressionWrapper(cantLibros_Prestado, output_field=CharField())).values('int_value')
    valor_entero = cantLibros_Prestado_int[0]['int_value']
    if valor_entero == 'Activo' :
        queryset.update(estadoReservacion =  'Cancelado' )
        messages.success(request, "La reservación seleccionada ha sido cancelada exitosamente")
    elif valor_entero != 'Activo' :
        messages.error(request, "La persona no tiene una reservación activa")


class ReservacionAdmin(admin.ModelAdmin):
    list_display = ('user','get_email','libroReservado','fechaReservación','estadoReservacion')
    search_fields = ('user','estadoReservacion')
    list_filter = ['user', 'estadoReservacion'] 
    actions = [cancelar_Reservacion]

    @admin.display(description='Email')
    def get_email(self, obj):
        return obj.user.user.email if obj.user.user else None
    
admin.site.site_header = 'Desa System'
admin.site.index_title = 'Sistema de Gestión Bibliotecario'
admin.site.site_title = 'Desa System'
admin.site.register(models.Reservacion, ReservacionAdmin)