from django.urls import path
from apps.autor.views import AutoresListado, AutoresDetalles

urlpatterns = [
    #path('autores/', AutoresListado.as_view(template_name = "autor/autor_list.html"), name='listado'),
    #path('autor/detalle/<int:pk>', AutoresDetalles.as_view(template_name = "autor/autor_detail.html"), name='detalles'),    
]