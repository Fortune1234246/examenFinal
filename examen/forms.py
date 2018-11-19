from django import forms
from .models import Materia, Grado

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ('materia', 'creditos', 'profesor')

class GradoForm(forms.ModelForm):
#todos los campos de Evento
    class Meta:
        model = Grado
        fields = ('grado', 'seccion', 'encargado', 'materias')
        def __init__ (self, *args, **kwargs):
            super(MateriaForm, self).__init__(*args, **kwargs)
            self.fields["asignacion"].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields["asignacion"].help_text = "Ingrese las materias"
            self.fields["asignacion"].queryset = Materia.objects.all()
