"""BAD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.menuPrincipal.views import index
from apps.autor.views import AutoresListado, AutoresDetalles
from apps.recurso.views import RecursosListado, RecursossDetalles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('autores/', AutoresListado.as_view(template_name = "autor/autor_list.html"), name='listadoAutores'),
    path('autor/detalle/<int:pk>', AutoresDetalles.as_view(template_name = "autor/autor_detail.html"), name='detallesAutores'),
    path('recursos/', RecursosListado.as_view(template_name = "recurso/recurso_list.html"), name='listadoRecursos'),
    path('recurso/detalle/<int:pk>', RecursossDetalles.as_view(template_name = "recurso/recurso_detail.html"), name='detalleRecursos'),
]
