from django.contrib import admin
from apps.prestamo import models
from django.contrib import messages
from django.db.models import F, IntegerField, ExpressionWrapper
from apps.prestamo.models import Prestamo
from django.contrib.auth.models import User

#@admin.action(permissions=["change"])
#@admin.action(description='Aumento de cantidad de Libros Prestados a la persona marcada')
#def realizar_Prestamo(modeladmin, request,obj ):    
#   usuario = Persona.objects.filter(user_id=3)
#    usuario.update(cantlibrosPrestados = F("cantlibrosPrestados")+1)
#    Persona.save
#    messages.success(request, "Aumento de cantidad de libros prestada exitosa")
from django.template.loader import render_to_string
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from datetime import datetime, timedelta


# Register your models here.
@admin.action(permissions=["change"], description='Notificar sobre vencimiento en plazo de préstamo')
def notificar_vencimiento(modeladmin, request, queryset):
    current_date = datetime.now().date()
    one_day = timedelta(days=1)

    for obj in queryset:
        # Calculate the difference between current date and fechaFinPrestamo
        date_difference = obj.fechaFinPrestamo - current_date

        if date_difference.days < 2 and obj.estadoPrestamo == 'Activo' :
            user_email = obj.user.user.email
            context = {'mail': user_email}
            html_content = render_to_string('correo.html', context)
            email_subject = 'Notificación de vencimiento en plazo de préstamo'
            email = EmailMultiAlternatives(email_subject, '', settings.EMAIL_HOST_USER, [user_email])
            email.attach_alternative(html_content, 'text/html')
            email.send()

notificar_vencimiento.short_description = 'Notificar vencimiento en plazo'

class PrestamoAdmin(admin.ModelAdmin):
    model = Prestamo
    list_display = ('user','get_email','get_cantLibros','libroPrestado','fechaInicioPrestamo','fechaFinPrestamo','fechaRealPrestamo','estadoPrestamo')
    search_fields = ('user','estadoPrestamo')
    list_filter = ['user', 'estadoPrestamo'] 
    date_hierarchy = 'fechaFinPrestamo'
    actions = [notificar_vencimiento]

    @admin.display(description='Cantidad de Libros Prestados')
    def get_cantLibros(self,obj):
        return obj.user.cantlibrosPrestados   
    
    @admin.display(description='Email')
    def get_email(self, obj):
        return obj.user.user.email if obj.user.user else None    

admin.site.site_header = 'Desa System'
admin.site.index_title = 'Sistema de Gestión Bibliotecario'
admin.site.site_title = 'Desa System'
admin.site.register(models.Prestamo, PrestamoAdmin)