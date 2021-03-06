from django.conf.urls import url
from . import views


#para llamar a nuestra página para insertar tenemos que invocar la dirección /pelicula/nueva

# se puede crear un hipervinculo para llamarla, en este ejemplo hay que invocar manualmente la dirección.

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^materia/listar/$', views.listar_materia, name='listar_materia'),
    url(r'^materia/new/$', views.crear_materia, name='crear_materia'),
    url(r'^grados/listar/$', views.listar_grados, name='listar_grados'),
    url(r'^grados/new/$', views.grados_new, name='grados_new'),
    ]
