#separa la logica de negocio del acceso a la base de datos

from canciones.models import Cancion

def obtener_todas():
                            #invesgitar de aqui estos metodos a donde los llama
    return Cancion.objects.all().order_by('id')

def crear_cancion(datos):
    Cancion.objects.create(**datos) #investigar por que el **

