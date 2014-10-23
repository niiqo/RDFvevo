from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('inasistencias.urls', namespace = "inasistencias")),
    url(r'^admin/', include(admin.site.urls)),
)
