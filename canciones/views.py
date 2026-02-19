from django.shortcuts import render,redirect,  get_object_or_404
from canciones.services import song_service #aqui estamos llamando el servicio
from canciones.forms import CancionForm

# metodos para las vistas
          #metodo http 
def index(request): 

    canciones = song_service.obtener_todas()  
    contexto = {'canciones': canciones} #diccionario clave valor
    return render(request, 'index.html', contexto) #peticion http y la redicreccion al index

def crear_cancion(request):

    if request.method == 'POST':
        form = CancionForm(request.POST)

        if form.is_valid(): #se valida en widgets
            song_service.crear_cancion(form.cleaned_data)
            return redirect('index')
    else:
        form = CancionForm()

    contexto = {'form': form, 'accion': 'Agregar Cancion'}

    return render(request, 'canciones_form.html', contexto)

def editar_cancion(request, id):

    cancion = get_object_or_404(song_service.obtener_todas(),pk=id)

    if request.method == 'POST':
        form = CancionForm(request.POST, instance=cancion)

        if form.is_valid(): #se valida en widgets
            song_service.editar_cancion(id, form.cleaned_data)
            return redirect('index')
    else:
        form = CancionForm(instance=cancion)

    contexto = {'form': form, 'accion': 'Editar Cancion'}

    return render(request, 'canciones_form.html', contexto)


def eliminar_cancion(request, id):

    if request.method == 'POST':
        song_service.eliminar_cancion(id)
    return redirect('index')
