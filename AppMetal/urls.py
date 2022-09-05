from django.urls import path
from AppMetal.views import *

urlpatterns = [
    path("", inicio, name= "inicio"),
    path("ingresante/", ingresantes, name= "ingresante"),
    path("graduado/", graduados, name= "graduado"),
    path("banda/", banda, name= "banda"),
    path("ingresantes/", ingreFormulario, name="ingreFormulario"),
    path("graduados/", graduadosFormulario, name="graduadosFormulario"),
    path("bandas/", bandasFormulario, name="bandasFormulario"),
    path("busquedaingresante/", busquedaIngresante, name="busquedaIngresante"),
    path("resultadoIngresante/", busquedaIngre, name="busquedaIngre"),
    path("busquedagraduado/", busquedaGraduado, name="busquedaGraduados"),
    path("resultadogradudado/", busquedaGra, name="busquedaGra"),
    path("busquedabanda/", busquedaBanda, name="busquedaBandas"),
    path("resultadobanda/", busquedaBan, name="busquedaBan"),
]