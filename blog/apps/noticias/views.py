from django.shortcuts import render,  HttpResponse, redirect
from.models import Noticia, Categoria,Contacto,Comentario
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView
from .forms import Form_Mod

# Create your views here.


from .forms import ContacotForm

#def inicio(request):
#  return HttpResponse(<h1>"Hola Mundo>"</h1>)


#decorador para ver la noticias como usario logueado

from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):
    # obener todas las noticias
    # ctx = {}
    # # clase.objets.all()==> select * from noticia
    # noticia = Noticia.objects.all()
    # ctx["noticias"] = noticia
    # return render(request, 'noticias/inicio.html', ctx)
    contexto={}
    id_categoria = request.GET.get('id',None)

    if id_categoria:
        n = Noticia.objects.filter(categoria_noticia = id_categoria)
        
    else:
        n= Noticia.objects.all() # una listacd..
    

    contexto['noticias'] = n
    
    
    cat = Categoria.objects.all().order_by('nombre')
    contexto['categorias'] = cat

    return render(request, 'noticias/inicio.html', contexto)

@login_required
def Detalle_Noticias(request, pk):
    contexto={}

    n= Noticia.objects.get(pk=pk)
    contexto['noticia'] = n

    c = Comentario.objects.filter(noticia=n)
    contexto['comentarios'] = c


    return render(request, 'noticias/detalle.html', contexto)


#Noticia.objects.all()               select * from noticias
#Noticia.objects.get(pk = 1)         select * from noticias where id = 1
#noticia.objects.filter(categoria)   select * from noticias where categoria = deportes

def contacto(request):
    data = {
        'form':ContacotForm()
    }
    if request.method == 'POST':

     ContacotForm(data=request.POST).save()
    return render(request, 'contacto/formulario.html', data)


@login_required
def Comentar_Noticia(request):
    comentario = request.POST.get('comentario', None)
    user = request.user
    noti = request.POST.get('id_noticia', None)
    noticia = Noticia.objects.get(pk=noti)
    coment = Comentario.objects.create( usuario=user, noticia=noticia, texto=comentario)
    return redirect(reverse_lazy('noticias:detalle', kwargs={"pk": noti}))

# modificar-eliminar comentarios


class BorrarComentario(DeleteView):
    model = Comentario
    template_name = "comentarios/comentario_confirm_delete.html"
    success_url = reverse_lazy("noticias:inicio")


class ModificaComentario(UpdateView):
    model = Comentario
    form_class = Form_Mod
    template_name = "comentarios/modificar.html"
    success_url = reverse_lazy("noticias:inicio")


@login_required
def Ordenar(request): 
    contexto={}
    id_categoria = request.GET.get('id',None)

    if id_categoria:
        n = Noticia.objects.filter(categoria_noticia = id_categoria).order_by('-fecha')
    else:
        n= Noticia.objects.all().order_by('-fecha') # una listacd..
    
    contexto['noticias'] = n    
    
    cat = Categoria.objects.all()

    return render(request, 'noticias/inicio.html', contexto)

@login_required
def Antiguos(request): 
    contexto={}
    id_categoria = request.GET.get('id',None)

    if id_categoria:
        n = Noticia.objects.filter(categoria_noticia = id_categoria).order_by('fecha')
    else:
        n= Noticia.objects.all().order_by('fecha') # una listacd..
    
    contexto['noticias'] = n    
    
    cat = Categoria.objects.all()

    return render(request, 'noticias/inicio.html', contexto)

@login_required
def ListarAZ(request): 
    contexto={}
    id_categoria = request.GET.get('id',None)

    if id_categoria:
        n = Noticia.objects.filter(categoria_noticia = id_categoria).order_by('titulo')
    else:
        n= Noticia.objects.all().order_by('titulo') # una listacd..
    
    contexto['noticias'] = n    
    
    cat = Categoria.objects.all()

    return render(request, 'noticias/inicio.html', contexto)

@login_required
def ListarZA(request): 
    contexto={}
    id_categoria = request.GET.get('id',None)

    if id_categoria:
        n = Noticia.objects.filter(categoria_noticia = id_categoria).order_by('-titulo')
    else:
        n= Noticia.objects.all().order_by('-titulo') # una listacd..
    
    contexto['noticias'] = n    
    
    cat = Categoria.objects.all()

    return render(request, 'noticias/inicio.html', contexto)
