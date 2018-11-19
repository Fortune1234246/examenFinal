from django.db import models

from django.contrib import admin





class Materia(models.Model):

    materia              = models.CharField(max_length=60)
    creditos             = models.IntegerField()
    profesor             = models.CharField(max_length=60)      #Para facilitar la aplicacion use profesor como atributo y no como tabla

    def __str__(self):

        return self.materia

class Grado(models.Model):

    grado              = models.CharField(max_length=60)
    seccion            = models.CharField(max_length=60)
    encargado          = models.CharField(max_length=60)        #del mismo modo use encargado como preofesor, pero sin usar relaciones
    materias           = models.ManyToManyField(Materia, through='asignacion')

    def __str__(self):

        return self.grado



class asignacion (models.Model):


    Grado               = models.ForeignKey(Grado, on_delete=models.CASCADE)

    Materia             = models.ForeignKey(Materia, on_delete=models.CASCADE)


class asignacionInLine(admin.TabularInline):

    model = asignacion

    extra = 1


class GradoAdmin(admin.ModelAdmin):

    inlines = (asignacionInLine,)


class MateriaAdmin (admin.ModelAdmin):

    inlines = (asignacionInLine,)
