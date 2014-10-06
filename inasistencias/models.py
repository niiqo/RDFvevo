from django.db import models

# Clase curso
class Curso():
    
    # Atributos de la clase
    numero = models.IntegerField("Curso",max_length=1)
    division = models.CharField("Division", max_lenght=1)
    anio = models.IntegerField("Curso",max_length=4)
    diasDeClase = models.IntegerField("Dias de Clase", max_length=2)

    # Metodos de la clase

    def __unicode__(self):
        curso = str(self.numero)+"º "+self.division+" "+self.anio
        return curso

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
