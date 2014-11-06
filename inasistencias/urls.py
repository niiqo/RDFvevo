from django.conf.urls import patterns, include, url
from RDFvevo import settings

urlpatterns = patterns('',

    url(r'^$', 'inasistencias.views.loguearse', name='login'),
    url(r'^desloguearse/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    
)
