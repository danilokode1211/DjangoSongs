#separa la logica de negocio del acceso a la base de datos

from canciones.models import Cancion

def obtener_todas():
                            #invesgitar de aqui estos metodos a donde los llama
    return Cancion.objects.all().order_by('id')

def crear_cancion(datos):

    Cancion.objects.create(**datos) #se hace doble asterisco para desempaquetar informacion

def editar_cancion(id,datos):
    cancion = Cancion.objects.get(pk=id) #obj ya existente y precargado
    for campo, valor in datos.items(): 
        setattr(cancion,campo,valor) #settear atributo
    cancion.save()

    return cancion

def eliminar_cancion(id):
    cancion = Cancion.objects.get(pk=id)
    cancion.delete()
        

