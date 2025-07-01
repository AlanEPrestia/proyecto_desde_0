from django.urls import path
from AppCoder.views.other import estudiantes, entregables, inicio, cursoFormulario2, busquedaCamada, buscar
from AppCoder.views.profesores import leerProfesores,eliminarProfesor,editarProfesor,profesorFormulario
from AppCoder.views.cursos import CursoCreateView,CursoDetailView,CursoDeleteView,CursoListView,CursoUpdateView

urlpatterns = [
    path('', inicio, name='inicio'),
    #path('cursos/', cursos, name='cursos'),
    #path('profesores/', profesores, name='profesores'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('entregables/', entregables, name='entregables'),

    path('cursoFormulario2/',cursoFormulario2,name='cursoFormulario2'),
    #path('profesorFormulario/',profesorFormulario,name="profesorFormulario"),

    path('busquedaCamada/', busquedaCamada, name="busquedaCamada"),
    path('buscar/', buscar, name='buscar'),

    path('profesores/',leerProfesores,name='profesores'),
    path('profesorFormulario/', profesorFormulario, name="profesorFormulario"),
    path('eliminarProfesor/<int:id_profesor>', eliminarProfesor, name="eliminarProfesor"),
    path('editarProfesor/<int:id_profesor>', editarProfesor, name="editarProfesor"),

    path('cursos/', CursoListView.as_view(), name='cursos'), 
    path('cursos/<int:pk>/', CursoDetailView.as_view(), name='cursos_detail'),
    path('cursos/nuevo/', CursoCreateView.as_view(), name='cursos_new'),
    path('cursos/editar/<int:pk>/', CursoUpdateView.as_view(), name='cursos_edit'),
    path('cursos/borrar/<int:pk>/', CursoDeleteView.as_view(), name='cursos_delete'),
]