from django.urls import path
from .views import cursos, profesores, estudiantes, entregables, inicio, cursoFormulario2, busquedaCamada, buscar

urlpatterns = [
    path('', inicio, name='inicio'),
    path('cursos/', cursos, name='cursos'),
    path('profesores/', profesores, name='profesores'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('entregables/', entregables, name='entregables'),

    path('cursoFormulario2/',cursoFormulario2,name='cursoFormulario2'),

    path('busquedaCamada/', busquedaCamada, name="busquedaCamada"),
    path('buscar/', buscar, name='buscar'),
]