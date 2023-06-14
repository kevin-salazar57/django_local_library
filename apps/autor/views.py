from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from .models import Autor 

#Clase para mostrar la vista de Lista de Autores
class AutoresListado(ListView): 
    model = Autor 

#Clase para mostrar la informacion en detalle del Autores
class AutoresDetalles(DetailView): 
    model = Autor