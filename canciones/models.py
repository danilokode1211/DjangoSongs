from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Cancion(models.Model):

    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    artista = models.CharField(max_length=100, verbose_name='Artista')
    
    popularidad = models.IntegerField(
    
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name='Popularidad (1,10)'
    )

    class Meta:

        db_table = 'cancion' #Nombre pintado en mysql       
        verbose_name ="Cancion"
        verbose_name_plural = 'Canciones'

    def __str__(self):
        return f"{self.titulo} - {self.artista}"  
