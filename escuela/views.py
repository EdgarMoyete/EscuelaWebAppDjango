from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
import csv
from django.template.loader import get_template
from xhtml2pdf import pisa

from .models import Carreras, Especialidades, Materias, Alumnos, Calificaciones
from .forms import CarreraForm, EspecialidadForm, MateriaForm, AlumnoForm, CalificacionForm

def index(request):
    return render(
        request,
        "index.html"
    )

# Carreras
class CarreraCreate(LoginRequiredMixin, CreateView):
    model = Carreras
    form_class = CarreraForm
    template_name = "create.html"
    success_url = reverse_lazy("carreras_read")

class CarreraList(LoginRequiredMixin, ListView):
    model = Carreras
    template_name = "carrerasRead.html"

    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'

class CarreraUpdate(LoginRequiredMixin, UpdateView):
    model = Carreras
    form_class = CarreraForm
    template_name = "create.html"
    success_url = reverse_lazy("carreras_read")

class CarreraDelete(LoginRequiredMixin, DeleteView):
    model = Carreras
    template_name = "confirmar.html"
    success_url = reverse_lazy("carreras_read")

# class CarreraDetail(DetailView):
#     model = Carreras
#     template_name = "carrerasSearch.html"

@login_required
def carrera_buscar_x_id(request):
    id = request.GET["id"]
    # SELECT *
    # FROM carreras
    # WHERE id_carrera = id
    # para evitar que truene cuando no regrese nada
    carrera = get_object_or_404(Carreras, id_carrera=id)
    return render(
        request,
        "carrerasSearch.html",
        {
            "object": carrera
        }
    )

# Especialidades
class EspecialidadCreate(LoginRequiredMixin, CreateView):
    model = Especialidades
    form_class = EspecialidadForm
    template_name = "create.html"
    success_url = reverse_lazy("especialidades_read")

class EspecialidadList(LoginRequiredMixin, ListView):
    model = Especialidades
    template_name = "especialidadesRead.html"

class EspecialidadUpdate(LoginRequiredMixin, UpdateView):
    model = Especialidades
    form_class = EspecialidadForm
    template_name = "create.html"
    success_url = reverse_lazy("especialidades_read")

class EspecialidadDelete(LoginRequiredMixin, DeleteView):
    model = Especialidades
    template_name = "confirmar.html"
    success_url = reverse_lazy("especialidades_read")

# class EspecialidadDetail(DetailView):
#     model = Especialidades
#     template_name = "especialidadesSearch.html"

@login_required
def especialidad_buscar_x_id(request):
    id = request.GET["id"]
    # SELECT *
    # FROM especialidads
    # WHERE id_especialidad = id
    # para evitar que truene cuando no regrese nada
    especialidad = get_object_or_404(Especialidades, id_especialidad=id)
    return render(
        request,
        "especialidadesSearch.html",
        {
            "object": especialidad
        }
    )

# Materias
class MateriaCreate(LoginRequiredMixin, CreateView):
    model = Materias
    form_class = MateriaForm
    template_name = "create.html"
    success_url = reverse_lazy("materias_read")

class MateriaList(LoginRequiredMixin, ListView):
    model = Materias
    template_name = "materiasRead.html"

class MateriaUpdate(LoginRequiredMixin, UpdateView):
    model = Materias
    form_class = MateriaForm
    template_name = "create.html"
    success_url = reverse_lazy("materias_read")

class MateriaDelete(LoginRequiredMixin, DeleteView):
    model = Materias
    template_name = "confirmar.html"
    success_url = reverse_lazy("materias_read")

# class MateriaDetail(DetailView):
#     model = Materias
#     template_name = "materiasSearch.html"

@login_required
def materia_buscar_x_id(request):
    id = request.GET["id"]
    # SELECT *
    # FROM materias
    # WHERE id_materia = id
    # para evitar que truene cuando no regrese nada
    materia = get_object_or_404(Materias, id_materia=id)
    return render(
        request,
        "materiasSearch.html",
        {
            "object": materia
        }
    )

# Alumnos
class AlumnoCreate(LoginRequiredMixin, CreateView):
    model = Alumnos
    form_class = AlumnoForm
    template_name = "create.html"
    success_url = reverse_lazy("alumnos_read")

class AlumnoList(LoginRequiredMixin, ListView):
    model = Alumnos
    template_name = "alumnosRead.html"

class AlumnoUpdate(LoginRequiredMixin, UpdateView):
    model = Alumnos
    form_class = AlumnoForm
    template_name = "create.html"
    success_url = reverse_lazy("alumnos_read")

class AlumnoDelete(LoginRequiredMixin, DeleteView):
    model = Alumnos
    template_name = "confirmar.html"
    success_url = reverse_lazy("alumnos_read")

# class AlumnoDetail(DetailView):
#     model = Alumnos
#     template_name = "alumnosSearch.html"

@login_required
def alumno_buscar_x_id(request):
    id = request.GET["id"]
    # SELECT *
    # FROM alumnos
    # WHERE id_alumno = id
    # para evitar que truene cuando no regrese nada
    alumno = get_object_or_404(Alumnos, id_alumno=id)
    return render(
        request,
        "alumnosSearch.html",
        {
            "object": alumno
        }
    )

# Calificaciones
class CalificacionCreate(LoginRequiredMixin, CreateView):
    model = Calificaciones
    form_class = CalificacionForm
    template_name = "create.html"
    success_url = reverse_lazy("calificaciones_read")

class CalificacionList(LoginRequiredMixin, ListView):
    model = Calificaciones
    template_name = "calificacionesRead.html"

class CalificacionUpdate(LoginRequiredMixin, UpdateView):
    model = Calificaciones
    form_class = CalificacionForm
    template_name = "create.html"
    success_url = reverse_lazy("calificaciones_read")

class CalificacionDelete(LoginRequiredMixin, DeleteView):
    model = Calificaciones
    template_name = "confirmar.html"
    success_url = reverse_lazy("calificaciones_read")

# class CalificacionDetail(DetailView):
#     model = Calificaciones
#     template_name = "calificacionesSearch.html"

@login_required
def calificacion_buscar_x_id(request):
    id = request.GET["id"]
    # SELECT *
    # FROM calificacions
    # WHERE id_calificacion = id
    # para evitar que truene cuando no regrese nada
    calificacion = get_object_or_404(Calificaciones, id_calificacion=id)
    return render(
        request,
        "calificacionesSearch.html",
        {
            "object": calificacion
        }
    )

# buscar alumno por CURP
@login_required
def buscar_x_curp(request):
    curp_busca = request.GET["curp"]
    # SELECT *
    # FROM alumnos
    # WHERE curp = curp
    # alumno = Alumnos.objects.get(curp=curp_busca)
    # para evitar que truene cuando no regrese nada
    alumno = get_object_or_404(Alumnos, curp=curp_busca)
    return render(
        request,
        "alumnosSearch.html",
        {
            "object": alumno
        }
    )

# buscar calificaciones mayores al umbral
@login_required
def mayores_calificaciones(request):
    umbral = request.GET["umbral"]
    # SELECT *
    # FROM calificaciones
    # WHERE calificacion > 95
    calificaciones = Calificaciones.objects.filter(calificacion__gt=umbral)
    # no se usa porque la linea de arriba no truena, muestra una tabla vacia
    # calificaciones = get_list_or_404(Calificaciones, calificacion__gt=umbral)
    
    return render(
        request,
        "calificacionesRead.html",
        {
            "object_list": calificaciones
        }
    )

@login_required
def boleta(request):
    id_alumno = request.GET["id"]
    # SELECT *
    # FROM calificaciones
    # WHERE id_alumno > ?
    calificaciones = Calificaciones.objects.filter(id_alumno=id_alumno)
    # SELECT *
    # FROM alumnos
    # WHERE id_alumno > ?
    alumno = get_object_or_404(Alumnos, id_alumno=id_alumno)
    return render(
        request,
        "boleta.html",
        {
            "object_list": calificaciones,
            "object": alumno
        }
    )

def csv_boleta(request, id_alumno):
    calificaciones = Calificaciones.objects.filter(id_alumno=id_alumno)
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="boleta.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow([
        'Materia',
        'Calificacion'
    ])
    for item in calificaciones:
        writer.writerow([item.id_materia, item.calificacion])
    return response

def pdf_boleta(request, id_alumno):
    calificaciones = Calificaciones.objects.filter(id_alumno=id_alumno)
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="boleta.pdf"'
    # find the template and render it.
    template = get_template("boletaPdf.html")
    html = template.render(
        {"object_list": calificaciones}
    )
    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)# link_callback=link_callback
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response