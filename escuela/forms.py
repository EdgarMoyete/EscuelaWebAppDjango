from django import forms
from .models import Carreras, Especialidades, Materias, Alumnos, Calificaciones

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carreras
        fields = '__all__'

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidades
        fields = '__all__'

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materias
        fields = '__all__'

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = '__all__'

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificaciones
        fields = '__all__'