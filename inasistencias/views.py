from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response

from inasistencias.models import Curso

#def ver_un_post(request, idpost):
#    post = Post.objects.get(id=idpost)
#    
#    return render_to_response("post.html",{"post":post,},)

def home(request):
    cursos = Curso.objects.order_by("numero")
    
    return render_to_response("home.html",{"cursos":cursos},)
