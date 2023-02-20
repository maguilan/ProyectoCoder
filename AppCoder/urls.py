from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('cursos/', cursos, name='cursos'),
    path('profesores/', profesores, name='profesores'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('entregables/', entregables, name='entregables'),
    path('curso-formulario', curso_formulario, name='curso-formulario'),
    path('profesor-formulario/', profesor_formulario, name='profesor-formulario')
]