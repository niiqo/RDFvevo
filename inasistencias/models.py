# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Curso(models.Model):
    # Atributos de la clase
    numero = models.IntegerField("Curso",max_length=1)
    division = models.CharField("Division", max_length=1)
    anio = models.IntegerField("Ciclo lectivo",max_length=4)
    diasDeClase = models.IntegerField("Dias de Clase", max_length=2)
    
    class Meta:
        ordering = ('-anio', 'numero', 'division')
    
    # Metodos de la clase
    def __unicode__(self):
        curso = str(self.numero)+" \""+str(self.division)+"\" - "+str(self.anio)
        return curso
    
    def color(self):
        if self.numero == 1:
            return 'blue'
        elif self.numero == 2:
            return 'green'
        elif self.numero == 3:
            return 'yellow'
        elif self.numero == 4:
            return 'red'
        elif self.numero == 5:
            return 'violet'
        elif self.numero == 6:
            return 'prueba'
        elif self.numero == 7:
            return 'gray'
    
    def getDiasDeClase(self):
        # Este metodo devuelve el total de dias de clases
        return self.diasDeClase
    
    def sumarDiasClase(self, cantDias):
        # Este metodo agrega dias de clase
        self.diasDeClase = (self.diasDeClase + cantDias)
    
    def getTotalAlumnos(self):
        # Este metodo devuelve el total de alumnos del curso
        cantidad = Alumno.count()
        return cantidad
    
    def getInasistencias(self):
        # Este metodo obtiene el total de inasistencias de el curso
        inasistencias = 0
        return inasistencias
    
    def getTotalAsistencias(self):
        # Este metodo calcula la cantidad total de asistencias
        # multiplicando el total de alumnos del curso por los dias de clase
        # y restando a ese resultado el total de inasistencias
        inasistencias = self.getInasistencias()
        totalAlumnos = self.getTotalAlumnos()
        dias = self.getDiasDeClase()
        totalAsistencias = ((totalAlumnos * dias) - inasistencias)
        return totalAsistencias
    
    def getAsistenciaMedia(self):
        # Este metodo calcula la asistencia media (total de asistencias sobre los dias de clase)
        asistencias = self.getTotalAsistencias()
        dias = self.getDiasDeClase()
        asistenciaMedia = (asistencias/dias)
        return asistenciaMedia
    
    def getPorcentajeAsistencia(self):
        # Este metodo devuelve el porcentaje de asistencias
        # dividiendo el numero de asistencias multiplicado por 100
        # en a cantidad de alumnos multiplicado por los dias de clase
        asistencias = (self.getTotalAsistencias * 100)
        alumnos = self.getTotalAlumnos()
        diasDeClase = self.getDiasDeClase()
        porcentajeDeAsistencia = (asistencias / (alumnos * diasDeClase))
        return porcentajeDeAsistencia

class Preceptor(User):
    cursos = models.ManyToManyField(Curso)
    
    class Meta:
        verbose_name = 'preceptor'
        verbose_name_plural = 'preceptores'
        
    # Similar a __str__, devuelve una descripcion mas amigable
    def __unicode__(self):
        return self.username
      
    def observar(self, alumno, descripcion):
        self.observacion_set.create(descripcion=descripcion)
        return descripcion

#Clase alumno:
class Alumno(User):
    # Atributos de la clase
    reincorporacion = models.IntegerField("Reincorporacion", max_length=2, default=0)
    dni = models.IntegerField("Dni", max_length=100, default=0)
    curso = models.ForeignKey(Curso)
    
    class Meta:
        verbose_name = 'alumno'
        verbose_name_plural = 'alumnos'

    # Similar a __str__, devuelve una descripcion mas amigable
    def __unicode__(self):
        return self.username
    
    # Devuelve todas las faltas del alumno
    def faltas(self):
        return self.inasistencia_set.all().count()

    # Devuelve todas las faltas injustificadas del alumno
    def injustificadas(self):
        return self.inasistencia_set.all().filter(justificado=False).count()
    
    # Devuelve todas las faltas justificadas del alumno
    def justificadas(self):
        return self.inasistencia_set.all().filter(justificado=True).count()
    
    # Devuelve todas las observaciones del alumno
    def observaciones(self):
        return self.observacion_set.count()

    # Devuelve todas las amonestaciones del alumno
    def amonestaciones(self):
        return self.amonestacion_set.count()

    
class Observacion (models.Model):
    descripcion = models.CharField(max_length=200)
    fecha = models.DateField(default=timezone.now())
    
    # relacion con el preceptor
    preceptor = models.ForeignKey(Preceptor)
    alumno = models.ForeignKey(Alumno)

    class Meta:
        verbose_name_plural = 'observaciones'
    
    # Similar a __str__, devuelve una descripcion mas amigable
    def __unicode__(self):
        return self.descripcion + self.fecha

class Amonestacion (models.Model):
    cantidad = models.IntegerField("Cantidad",max_length=2)
    descripcion = models.CharField(max_length=200)
    fecha = models.DateField(default=timezone.now())
    
    # relacion con el preceptor
    preceptor = models.ForeignKey(Preceptor)
    alumno = models.ForeignKey(Alumno)

    class Meta:
        verbose_name_plural = 'amonestaciones'
    
    # Similar a __str__, devuelve una descripcion mas amigable
    def __unicode__(self):
        return self.cantidad + self.descripcion + self.fecha

class Inasistencia (models.Model):
    tipo = models.FloatField()
    justificado = models.BooleanField(default=False)
    fecha = models.DateField()
    preceptor = models.ForeignKey(Preceptor)
    alumno = models.ForeignKey(Alumno)
    
    # Similar a __str__, devuelve una descripcion mas amigable
    def __unicode__(self):
        return self.fecha.__str__()
