from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppMetal.forms import *

def inicio(request):
    return render(request, "AppMetal/inicio.html")

def ingresantes(request):
    return render(request, "AppMetal/ingresantes.html")

def graduados(request):
    return render(request, "AppMetal/graduados.html")

def banda(request):
    return render(request, "AppMetal/banda.html")

def ingreFormulario(request):
    if request.method=="POST":
        form=IngresantesForm(request.POST)
        print("-----------------")
        print(form)
        print("-----------------")
        if form.is_valid():
            infomacion=form.cleaned_data
            print(infomacion)
            nombre=infomacion["nombre"]
            apellido=infomacion["apellido"]
            ingre=Ingresantes(nombre=nombre, apellido=apellido)
            ingre.save()
            return render (request, "AppMetal/inicio.html", {"mensaje":"Creado"})
    else:
        form=IngresantesForm
        return render (request, "AppMetal/ingreFormulario.html", {"formulario":form})


def graduadosFormulario(request):
    if request.method=="POST":
        form= GraduadosForm(request.POST)
        print("-----------------")
        print(form)
        print("-----------------")
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            graduado=Graduados(nombre=nombre, apellido=apellido)
            graduado.save()
            return render (request, "AppMetal/inicio.html", {"mensaje":"Creado"})
    else:
        form=GraduadosForm
        return render (request, "AppMetal/graduadosformulario.html", {"formulario":form})


def bandasFormulario(request):
    if request.method=="POST":
        form= BandasForm(request.POST)
        print("-----------------")
        print(form)
        print("-----------------")
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            comision=informacion["comision"]
            banda=Bandas(nombre=nombre, comision=comision)
            banda.save()
            return render (request, "AppMetal/inicio.html", {"mensaje":"Creado"})
    else:
        form=BandasForm
        return render (request, "AppMetal/bandasFormulario.html", {"formulario":form})



def busquedaIngresante(request):
    return render(request, "Appmetal/busquedaIngresante.html")

def busquedaIngre(request):
    if request.GET["nombre"]:
       nombre=request.GET["nombre"]
       ingresante=Ingresantes.objects.filter(nombre=nombre)
       return render (request, "AppMetal/resultadoIngresante.html", {"ingresante":ingresante})
    else:
        return render(request, "AppMetal/busquedaIngresante.html", {"mensaje":"Ingrese una nombre valido"})
    


def busquedaGraduado(request):
    return render(request, "Appmetal/busquedaGraduados.html")

def busquedaGra(request):
    if request.GET["graduado"]:
       nombre=request.GET["graduado"]
       graduado=Graduados.objects.filter(nombre=nombre)
       return render (request, "AppMetal/resultadoGraduado.html", {"graduado":graduado})
    else:
        return render(request, "AppMetal/busquedaGraduado.html", {"mensaje":"Ingrese una nombre valido"})
    
    

def busquedaBanda(request):
    return render(request, "Appmetal/busquedaBanda.html")

def busquedaBan(request):
    if request.GET["comision"]:
       comision=request.GET["comision"]
       curso=Bandas.objects.filter(comision=comision)
       return render (request, "AppMetal/resultadoBanda.html", {"cursos":curso})
    else:
        return render(request, "AppMetal/busquedaBanda.html", {"mensaje":"Ingrese una nombre valido"})
    
    