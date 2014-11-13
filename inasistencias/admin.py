# -*- coding: utf-8 -*-

from django.contrib import admin
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from inasistencias.models import Preceptor, Curso, Alumno, Inasistencia
from django.utils.translation import ugettext_lazy as _


class PreceptorForm(UserChangeForm):
    password = forms.CharField(label=_("Password"),
	widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
	widget=forms.PasswordInput,
	help_text=_("Enter the same password as above, for verification."))
    
    class Meta:
	model = Preceptor
	fields = ('username', 'password', 'password2', 'cursos', 'first_name', 'last_name', 'email')

class PreceptorAddForm(UserCreationForm):
    class Meta:
	model = Preceptor
	fields = ('username', 'password1', 'password2', 'cursos', 'first_name', 'last_name', 'email')


class AlumnoForm(UserChangeForm):
    password = forms.CharField(label=_("Password"),
	widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
	widget=forms.PasswordInput,
	help_text=_("Enter the same password as above, for verification."))
    
    class Meta:
	model = Alumno
	fields = ('username', 'password', 'password2', 'curso', 'first_name', 'last_name', 'email')

class AlumnoAddForm(UserCreationForm):
    class Meta:
	model = Alumno
	fields = ('username', 'password1', 'password2', 'curso', 'first_name', 'last_name', 'email')


class PreceptorAdmin(admin.ModelAdmin):
    form = PreceptorForm
    add_form = PreceptorAddForm
    
    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            return PreceptorAddForm
        else:
            return super(PreceptorAdmin, self).get_form(request, obj, **kwargs)

class AlumnoAdmin(admin.ModelAdmin):
    form = AlumnoForm
    add_form = AlumnoAddForm
    
    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            return AlumnoAddForm
        else:
            return super(AlumnoAdmin, self).get_form(request, obj, **kwargs)

class CursoAdmin(admin.ModelAdmin):
    list_filter = ('anio',)

admin.site.register(Preceptor, PreceptorAdmin)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Inasistencia)