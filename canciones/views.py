from django.shortcuts import render
from canciones.services import song_service

# metodos para las vistas
          #metodo http 
def index(request): 

    canciones = song_service.obtener_todas()  
    contexto = {'canciones': canciones} #diccionario clave valor
    return render(request, 'index.html', contexto) #peticion http y la redicreccion al index



