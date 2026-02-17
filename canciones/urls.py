from django.urls import path
from . import views


urlpatterns = [
                    #referencia al index. html buscado en templates
    path('', views.index, name='index'),
    path('agregar/', views.crear_cancion, name='crear_cancion')
    
]