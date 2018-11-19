from django.shortcuts import render
from examen.models import Materia, Grado
from .forms import MateriaForm, GradoForm
from django.shortcuts import redirect
from django.contrib import messages

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

def grados_new(request):
    if request.method == "POST":
        formulario = GradoForm(request.POST)
        if formulario.is_valid():
            venta = Grado.objects.create(grado=formulario.cleaned_data['grado'], seccion=formulario.cleaned_data['seccion'], encargado=formulario.cleaned_data['encargado'])
            for carro_id in request.POST.getlist('carro'):
                detalleVenta = detalleVenta(carro_id=carro_id, venta_id = venta.id)
                detalleVenta.save()
            messages.add_message(request, messages.SUCCESS, 'Venta hecha exitosamente')
    else:
        formulario = GradoForm()
    return render(request, 'examen/grados_new.html', {'formulario': formulario})
