from django.shortcuts import render
from examen.models import Materia

# Create your views here.


def listar_materia(request):
    materia = Materia.objects.all()
    return render(request, 'examen/listarmaterias.html', {'materia': materia})
