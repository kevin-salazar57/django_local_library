from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from .models import Recurso 

# Create your views here.
#Clase para mostrar la vista de Lista de Recursos
class RecursosListado(ListView): 
    model = Recurso 

#Clase para mostrar la informacion en detalle del Recurso
class RecursossDetalles(DetailView): 
    model = Recurso