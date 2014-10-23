# -*- coding: utf-8 -*-

from django.contrib import admin
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from inasistencias.models import Preceptor, Curso, Observacion, Inasistencia, Alumno


class UserForm (UserCreationForm):
    class Meta:
	model = User
	fields = ('first_name', 'last_name', 'email', 'username')

class UserAdmin(admin.ModelAdmin):
    form = UserForm
    
    
admin.site.register(Observacion)
admin.site.register(Inasistencia)
admin.site.register(Preceptor, UserAdmin)
admin.site.register(Alumno, UserAdmin)
admin.site.register(Curso)