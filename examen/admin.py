from django.contrib import admin
from .models import *

admin.site.register(Materia, MateriaAdmin)
admin.site.register(Grado, GradoAdmin)
admin.site.register(asignacion)
