from django.urls import path
from . import views

app_name = 'noticias'

#Urls de app noticias
urlpatterns = [
    
    path('', views.inicio, name='inicio'),
    #Detalle de la noticias por pk
    path('detalle<int:pk>', views.Detalle_Noticias,name ='detalle'),

    #url del formulario de contacto
    path('contacto', views.contacto, name="contacto"),

    # URL COMENTARIO
    path('comentario', views.Comentar_Noticia, name='comentar'),
    
    # eliminar comentario
    path('Borrar/<int:pk>', views.BorrarComentario.as_view(),
         name="borrar_comentario"),
    # modificar comentario
    path("Modificar/<int:pk>", views.ModificaComentario.as_view(),
         name="modificar_comentario"),
    #Orden por fecha
    path('ordenar', views.Ordenar, name='ordenar'),
    #Orden mas antiguos
    path('antiguos', views.Antiguos, name='antiguos'),

    #Orden A-Z
    path('listar', views.ListarAZ, name='listar'),     
     #Orden Z-z-A
    path('listarza', views.ListarZA, name='listarza')
    
]