from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.template.defaulttags import NowNode
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.decorators import login_required

from inasistencias.templatetags.faltas import formatear_fecha
from inasistencias.models import Curso, Preceptor, Alumno, Curso, Inasistencia

import datetime


@login_required(login_url="/loguearse")
def home(request):
    context = RequestContext(request)
    
    # Si es Administrador
    if request.user.is_staff:
	return render_to_response('admin/administrador.html', {'usuario': request.user, 'cursos': Curso.objects.all()}, context)
    
    # Si es Preceptor
    elif es_preceptor(request.user):
	return render_to_response('preceptor/preceptor.html', {'usuario': request.user, 'cursos': Curso.objects.all().filter(preceptor=request.user)}, context)
    
    # Si es Alumno
    elif es_alumno(request.user):
	return render_to_response('alumno/alumno.html', {'usuario': request.user}, context)
    
    # Sino
    else:
	return HttpResponse('ERROR')

def loguearse(request):
    context = RequestContext(request)
	
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
	# Usuario y contrasena
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username=username, password=password)

	if user:
	    # Is the account active? It could have been disabled.
	    if user.is_active:
		# If the account is valid and active, we can log the user in.
		# We'll send the user back to the homepage.
		login(request, user)

		return redirect('/')

	    else:
		# An inactive account was used - no logging in!
		return HttpResponse("ERROR: cuenta inactiva.")
	else:
	    # Bad login details were provided. So we can't log the user in.
	    print "Invalid login details: {0}, {1}".format(username, password)
	    return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
	# No context variables to pass to the template system, hence the
	# blank dictionary object...
	
	return render_to_response('login.html', context)

def desloguearse(request):
    logout(request)
    
    return redirect('/loguearse')

@login_required(login_url="/loguearse")
def curso(request, id_curso):
    fecha = NowNode("SHORT_DATE_FORMAT").render(None)
    alumnos = Alumno.objects.all().filter(curso_id=id_curso)
    
    if request.method == 'POST':
	print request.POST
	
	if request.POST.get('cargar'):
	    fecha = request.POST['fecha']
	
	if request.POST.get('guardar'):
	    fecha = request.POST['fecha']
	    preceptor = request.POST['preceptor']
	    
	    registrar_faltas(fecha, alumnos, request.POST, preceptor)
		
    
    # Si es preceptor
    if es_preceptor(request.user):
	return render_to_response('preceptor/curso.html', {'usuario': request.user, 'alumnos': alumnos, 'curso': Curso.objects.get(id=id_curso), 'dia': fecha}, RequestContext(request))

    # Sino
    else:
	return HttpResponse('Necesitas estar logueado como preceptor para ver esto...')

@login_required(login_url="/loguearse")
def alumno(request, id_alumno):
    
    # Si es preceptor
    if es_preceptor(request.user):
	return render_to_response('preceptor/alumno.html', {'usuario': request.user, 'alumno': Alumno.objects.get(id=id_alumno)}, RequestContext(request))

    # Sino
    else:
	return HttpResponse('Necesitas estar logueado como preceptor para ver esto...')

@login_required(login_url="/loguearse")
def info(request, id_curso):
    
    # Si es preceptor
    if es_preceptor(request.user):
	return render_to_response('preceptor/info.html', {'usuario': request.user, 'curso': Curso.objects.get(id=id_curso)}, RequestContext(request))

    # Sino
    else:
	return HttpResponse('Necesitas estar logueado como preceptor para ver esto...')




# Devuelve true si es preceptor
def es_preceptor(usuario):
    try:
	Preceptor.objects.get(pk=usuario.pk)
	return True
    except:
	return False

# Devuelve true si es alumno
def es_alumno(usuario):
    try:
	Alumno.objects.get(pk=usuario.pk)
	return True
    except:
	return False

# Leva a cabo el registro de faltas de una lista de alumnos
def registrar_faltas(fecha, alumnos, post, preceptor):
    fecha = formatear_fecha(fecha)
    dic = {
      'P': None,
      '1/2': 0.5,
      '1/4': 0.25,
      '3/4': 0.75,
      'A': 1,
    }

    for al in alumnos:
	falta = Inasistencia.objects.filter(alumno=al).filter(fecha=fecha)
	# Tipo de inasistencia
	tipo = post[str(al.id)]
	
	# Si existe una falta de ese alumno en esa fecha
	if falta:
	    
	    # Si el tipo de falta coincide 
	    if dic[tipo] == falta[0].tipo:
		print 'iguales'
		
	    # Si no coincide
	    elif dic[tipo] != falta[0].tipo:
		# Si se corrijio a presente
		if not dic[tipo]:
		    falta[0].delete()

		# Si se cambio el valor de la falta
		else:
		    falta[0].tipo = dic[tipo]
		    falta[0].save()
		    
		    print 'distintos'
	
	# Si no existe una falta de ese alumno en esa fecha, y no estuvo presente, se crea
	elif tipo != 'P':
	    fal = Inasistencia(tipo=dic[tipo], alumno=al, preceptor=Preceptor.objects.get(username=preceptor), fecha=fecha)
	    fal.save()
	    print 'creada'
	    



