from django.contrib import admin
from inasistencias.models import Preceptor, Curso


#class PreceptorAdmin(admin.ModelAdmin):
    # Informacion que se muestra en la lista
    #list_display = ('username', 'password')
    # Busqueda por titulo
    #search_fields = ['username']

admin.site.register(Preceptor)#, PreceptorAdmin)
admin.site.register(Curso)
