from django.views.generic import ListView # Importamos ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from AppCoder.models import Curso


class CursoListView(ListView):
    """
    Vista para listar todos los cursos.
    """
    model = Curso
    template_name = 'AppCoder/cursos/curso_list.html'
    #paginate_by = 10                # Paginación: 10 cursos por página
    #ordering = ['camada',]  # Ordenar por camada (descendente) y luego por nombre (ascendente)


class CursoDetailView(DetailView):
    """
    Vista para mostrar los detalles de un curso específico.
    """
    model = Curso
    template_name = 'AppCoder/cursos/curso_detail.html'

class CursoCreateView(CreateView):
    """
    Vista para crear un nuevo curso.
    """
    model = Curso
    fields = ['nombre', 'camada']
    template_name = 'AppCoder/cursos/curso_form.html'
    success_url = '/app/cursos/'  # Redirige a la lista de cursos después de crear uno nuevo
    

class CursoUpdateView(UpdateView):
    """
    Vista para actualizar un curso existente.
    """
    model = Curso
    fields = ['nombre', 'camada']
    template_name = 'AppCoder/cursos/curso_form.html'
    success_url = '/app/cursos/' 


class CursoDeleteView(DeleteView):
    """
    Vista para eliminar un curso existente.
    """
    model = Curso
    template_name = 'AppCoder/cursos/curso_confirm_delete.html'
    success_url = '/app/cursos/'