from django.shortcuts import render
from examen.models import Materia, Grado
from .forms import MateriaForm
from django.shortcuts import redirect

# Create your views here.


def listar_materia(request):
    materia = Materia.objects.all()
    return render(request, 'examen/listarmaterias.html', {'materia': materia})

def crear_materia(request):
    if request.method == "POST":
        form = MateriaForm(request.POST)
        if form.is_valid():
            carro = form.save(commit=False)
            carro.save()
            return redirect('listar_materia')
    else:
        form = MateriaForm()
        return render(request, 'examen/materia_new.html', {'form': form})

def listar_grados(request):
    venta = Grado.objects.all()
    return render(request, 'examen/listargrados.html', {'venta': venta})
