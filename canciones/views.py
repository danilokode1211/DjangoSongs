from django.shortcuts import render

# metodos para las vistas
          #metodo http 
def index(request): 

    return render(request, 'index.html') #peticion http y la redicreccion al index



