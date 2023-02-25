# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Carreras(models.Model):
    id_carrera = models.AutoField(primary_key=True)
    carrera = models.CharField(max_length=50)

    def __str__(self): # se puede agregar str(self.id)
        return self.carrera
    
    class Meta: # por usar inspectdb
        managed = False
        db_table = 'carreras'

class Especialidades(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    especialidad = models.CharField(max_length=50)
    id_carrera = models.ForeignKey(
        Carreras,
        models.DO_NOTHING,
        db_column='id_carrera',
        blank=True,
        null=True,
        # on_delete=models.CASCADE # talvez no
    )

    def __str__(self): # se puede agregar str(self.id)
        return self.especialidad
    
    class Meta: # por usar inspectdb
        managed = False
        db_table = 'especialidades'

class Materias(models.Model):
    id_materia = models.AutoField(primary_key=True)
    materia = models.CharField(max_length=50)
    id_carrera = models.ForeignKey(
        Carreras,
        models.DO_NOTHING,
        db_column='id_carrera',
        blank=True,
        null=True,
        # on_delete=models.CASCADE # talvez no
    )

    def __str__(self): # se puede agregar str(self.id)
        return self.materia
    
    class Meta: # por usar inspectdb
        managed = False
        db_table = 'materias'

class Alumnos(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30, blank=True, null=True)
    nombres = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    curp = models.CharField(max_length=18, blank=True, null=True)
    id_carrera = models.ForeignKey(
        'Carreras',
        models.DO_NOTHING,
        db_column='id_carrera',
        blank=True,
        null=True,
        # on_delete=models.CASCADE # talvez no
    )
    id_especialidad = models.ForeignKey(
        'Especialidades',
        models.DO_NOTHING,
        db_column='id_especialidad',
        blank=True,
        null=True,
        # on_delete=models.CASCADE # talvez no
    )

    def __str__(self): # se puede agregar str(self.id)
        return ( # solo datos != None
            self.apellido_paterno + " " +
            self.nombres
        )
    
    class Meta: # por usar inspectdb
        managed = False
        db_table = 'alumnos'

class Calificaciones(models.Model):
    id_calificacion = models.AutoField(primary_key=True)
    calificacion = models.FloatField()
    id_alumno = models.ForeignKey(
        Alumnos,
        models.DO_NOTHING,
        db_column='id_alumno',
        blank=True,
        null=True,
        # on_delete=models.CASCADE # talvez no
    )
    id_materia = models.ForeignKey(
        'Materias',
        models.DO_NOTHING,
        db_column='id_materia',
        blank=True,
        null=True,
        # on_delete=models.CASCADE # talvez no
    )

    def __str__(self): # se puede agregar str(self.id)
        return str(self.calificacion)
    
    class Meta: # por usar inspectdb
        managed = False
        db_table = 'calificaciones'