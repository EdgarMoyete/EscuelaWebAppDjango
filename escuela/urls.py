from django.urls import path
from .views import (
    index,
    CarreraCreate, CarreraList, CarreraUpdate, CarreraDelete, carrera_buscar_x_id,
    EspecialidadCreate, EspecialidadList, EspecialidadUpdate, EspecialidadDelete, especialidad_buscar_x_id,
    MateriaCreate, MateriaList, MateriaUpdate, MateriaDelete, materia_buscar_x_id,
    AlumnoCreate, AlumnoList, AlumnoUpdate, AlumnoDelete, alumno_buscar_x_id,
    CalificacionCreate, CalificacionList, CalificacionUpdate, CalificacionDelete, calificacion_buscar_x_id,
    buscar_x_curp, mayores_calificaciones, boleta, csv_boleta, pdf_boleta
)

urlpatterns = [
    path('', index, name='index'),
    
    path('carreras_create/', CarreraCreate.as_view(), name='carreras_create'),
    path('carreras_read/', CarreraList.as_view(), name='carreras_read'),
    path('carreras_update/<int:pk>/', CarreraUpdate.as_view(), name='carreras_update'),
    path('carreras_delete/<int:pk>/', CarreraDelete.as_view(), name='carreras_delete'),
    path('carreras_search/', carrera_buscar_x_id, name='carreras_search'),

    path('especialidades_create/', EspecialidadCreate.as_view(), name='especialidades_create'),
    path('especialidades_read/', EspecialidadList.as_view(), name='especialidades_read'),
    path('especialidades_update/<int:pk>/', EspecialidadUpdate.as_view(), name='especialidades_update'),
    path('especialidades_delete/<int:pk>/', EspecialidadDelete.as_view(), name='especialidades_delete'),
    path('especialidades_search/', especialidad_buscar_x_id, name='especialidades_search'),

    path('materias_create/', MateriaCreate.as_view(), name='materias_create'),
    path('materias_read/', MateriaList.as_view(), name='materias_read'),
    path('materias_update/<int:pk>/', MateriaUpdate.as_view(), name='materias_update'),
    path('materias_delete/<int:pk>/', MateriaDelete.as_view(), name='materias_delete'),
    path('materias_search/', materia_buscar_x_id, name='materias_search'),

    path('alumnos_create/', AlumnoCreate.as_view(), name='alumnos_create'),
    path('alumnos_read/', AlumnoList.as_view(), name='alumnos_read'),
    path('alumnos_update/<int:pk>/', AlumnoUpdate.as_view(), name='alumnos_update'),
    path('alumnos_delete/<int:pk>/', AlumnoDelete.as_view(), name='alumnos_delete'),
    path('alumnos_search/', alumno_buscar_x_id, name='alumnos_search'),

    path('calificaciones_create/', CalificacionCreate.as_view(), name='calificaciones_create'),
    path('calificaciones_read/', CalificacionList.as_view(), name='calificaciones_read'),
    path('calificaciones_update/<int:pk>/', CalificacionUpdate.as_view(), name='calificaciones_update'),
    path('calificaciones_delete/<int:pk>/', CalificacionDelete.as_view(), name='calificaciones_delete'),
    path('calificaciones_search/', calificacion_buscar_x_id, name='calificaciones_search'),
                                                                       
    path('buscar_curp/', buscar_x_curp, name='buscar_curp'),
    path('mayores_calificaciones/', mayores_calificaciones, name='mayores_calificaciones'),
    path('boleta/', boleta, name='boleta'),
    path('csv_boleta/<id_alumno>/', csv_boleta, name='csv_boleta'),
    path('pdf_boleta/<id_alumno>/', pdf_boleta, name='pdf_boleta'),
]