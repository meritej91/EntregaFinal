from django.urls import path
from veterinaria.views import *

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("clinica/", clinica, name="clinica"),
    path("paciente/", paciente, name="paciente"),
    path("estudio/", estudio, name="estudio"),
    path("turno/", turno, name="turno"),
]
