from django.shortcuts import render
from ..models import Curso,Profesor
from ..forms import CursoFormulario, ProfesorFormulario
from django.http import HttpResponse


def inicio(request):
    return render(request, "AppCoder/index.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def cursoFormulario2(request):
      if request.method == "POST":
            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                  curso.save()
                  return render(request, "AppCoder/cursos.html")
      else:
            miFormulario = CursoFormulario() # Formulario vacio para construir el html
 
      return render(request, "AppCoder/formulario/cursoFormulario2.html", {"miFormulario": miFormulario})


def busquedaCamada(request):
    return render(request, "AppCoder/formulario/busquedaCamada.html")


def buscar(request):
    if request.GET["camada"]:
        #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }"
        camada = request.GET['camada']
        # icontains es un filtro que se usa para buscar coincidencias en los campos de texto de la base de datos, 
        # sin importar si las letras están en mayúsculas o minúsculas
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, "AppCoder/formulario/resultadosBusqueda.html", {"cursos": cursos, "camada": camada})

    else:
        respuesta = "No enviaste datos"

        # No olvidar from django.http import HttpResponse
        return HttpResponse(respuesta)
    
def profesorFormulario(request):

    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)  # aquí llega toda la información del html
        if miFormulario.is_valid():  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            profesor = Profesor(
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                email=informacion['email'],
                profesion=informacion['profesion']
            )
            profesor.save()
            return render(request, "AppCoder/index.html")  # Vuelvo al inicio o a donde quieran
    else:
        miFormulario = ProfesorFormulario()  # Formulario vacío para construir el html

    return render(request, "AppCoder/formulario/profesorFormulario.html", {"miFormulario": miFormulario})
