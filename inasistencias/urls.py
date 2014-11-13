from django.conf.urls import patterns, include, url
from RDFvevo import settings

urlpatterns = patterns('',

    url(r'^$', 'inasistencias.views.home', name='home'),
    url(r'^loguearse/$', 'inasistencias.views.loguearse', name='loguearse'),
    url(r'^desloguearse/$', 'inasistencias.views.desloguearse', name='desloguearse'),
    url(r'^curso/(?P<id_curso>\d+)/$', 'inasistencias.views.curso', name='curso'),
    url(r'^curso/(?P<id_curso>\d+)/info/$', 'inasistencias.views.info', name='informacion'),
    url(r'^alumno/(?P<id_alumno>\d+)/$', 'inasistencias.views.alumno', name='alumno'),
    
)
