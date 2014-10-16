# -*- coding: utf-8 -*-

from django.contrib import admin
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from rdf.models import Preceptor, Curso, Observacion, Inasistencia, Alumno


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

#admin.site.unregister(User)
#admin.site.unregister(Group)

p = [{'username': 'claudio',
      'first_name': 'Claudio',
      'last_name': 'Cavestri',
      'email': 'claudito@gmail.com',
      },
      {'username': 'poli',
      'first_name': 'Pablo',
      'last_name': 'Palavecino',
      'email': 'polito@gmail.com',
      },
      {'username': 'juan',
      'first_name': 'Juan',
      'last_name': 'Portis',
      'email': 'donbosco@gmail.com',
      }]

a = [{'username': 'lucho',
      'first_name': 'Luciano',
      'last_name': 'Castillo',
      'email': 'claudito@gmail.com',
      },
      {'username': 'arabe',
      'first_name': 'Augusto',
      'last_name': 'Jair',
      'email': 'polito@gmail.com',
      },
      {'username': 'many',
      'first_name': 'Nicolas',
      'last_name': 'Ordoñez',
      'email': 'donbosco@gmail.com',
      }]

for i in range(3):
    username = p[i]['username']
    first_name = p[i]['first_name']
    last_name = p[i]['last_name']
    email = p[i]['email']
    print username
    pre = Preceptor(username=username, first_name=first_name, last_name=last_name, email=email)
    pre.save()

    username = a[i]['username']
    first_name = a[i]['first_name']
    last_name = a[i]['last_name']
    email = a[i]['email']

    print username
    al = Alumno(username=username, first_name=first_name, last_name=last_name, email=email)
    al.save()









