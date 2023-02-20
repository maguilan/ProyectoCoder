from django.shortcuts import render, redirect
from .forms import CursoFormulario, ProfesorFormulario
from .models import Curso, Profesor

#from AppCoder.models import Curso

# Create your views here.

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursos(request):
    return render(request, 'AppCoder/cursos.html')

def profesores(request):
    
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')

def curso_formulario(request):

    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nuevo_curso = Curso(nombre = informacion['nombre'], camada = informacion['camada'])
            nuevo_curso.save()
            return redirect('inicio')

        
    mi_formulario = CursoFormulario()
    return render(request, 'AppCoder/curso-formulario.html', {'formulario_curso': mi_formulario})


def profesor_formulario(request):

    if request.method == 'POST':
        mi_formulario = ProfesorFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            profesor = Profesor(nombre = informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'], profesion = informacion['profesion'])
            profesor.save()
            return redirect('inicio')

        
    mi_formulario = ProfesorFormulario()
    return render(request, 'AppCoder/profesor-formulario.html', {'formulario_profesor': mi_formulario})






