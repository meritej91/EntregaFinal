from django.shortcuts import render
from django.http import HttpResponse 
from veterinaria.models import Clinica
from veterinaria.models import Estudio
from veterinaria.models import Paciente
from veterinaria.models import Turno

def inicio(request):
    return render(request, "veterinaria/inicio.html")

def clinica(request):
    return render(request, "veterinaria/clinica.html")

def paciente(request):
    return render(request, "veterinaria/paciente.html")

def estudio(request):
    return render(request, "veterinaria/estudio.html")

def turno(request):
    return render(request, "veterinaria/turno.html")
