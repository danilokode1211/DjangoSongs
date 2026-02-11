from django.urls import path
from . import views


urlpatterns = [
                    #referencia al index. html buscado en templates
    path('', views.index, name='index'),
]