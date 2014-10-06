from django.conf.urls import patterns, include, url
from blog import settings

urlpatterns = patterns('',
#    url(
#         r'^post/(?P<idpost>[0-9]+)/$',
#         'post.views.ver_un_post', 
#         name="ver_un_post"),
    url(
         r'^$',
         'inasistencias.views.home',
         name='home'),
)

urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL, 'show_indexes': True}),
)
