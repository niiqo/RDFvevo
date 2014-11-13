from django import template
from inasistencias.models import Alumno, Inasistencia

register = template.Library()

@register.simple_tag
def chequear(alumno, fecha, tipo):
    dic = {
      'P': None,
      '1/2': 0.5,
      '1/4': 0.25,
      '3/4': 0.75,
      'A': 1,
    }
    
    fecha = formatear_fecha(fecha)
    
    falta = Inasistencia.objects.filter(alumno=alumno).filter(fecha=fecha)
    
    # Si existe una falta de ese alumno en esa fecha
    if falta:
	# Si el tipo de falta coincide activa esa opcion
	if dic[tipo] == falta[0].tipo:
	    return 'checked'
	else:
	    return ''

    # Si no hay falta para esa fecha y la opcion es presente
    elif tipo == 'P':
	# Se activa
	return 'checked'

    else:
	return ''


def formatear_fecha(fecha):
    if fecha.find('/'):
	f = fecha.split('/')
	return f[2] + '-' + f[1] + '-' + f[0]
    else:
	return fecha