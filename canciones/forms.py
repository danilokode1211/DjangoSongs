from django import forms
from canciones.models import Cancion

class CancionForm(forms.ModelForm):
    class Meta:

        model = Cancion #modelo asociado
        fields= ['titulo', 'artista', 'popularidad']

        widgets = {
            #preguntar si jode por identacion
            'titulo': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el título'
            }),
            'artista': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el artista'
            }),
            'popularidad': forms.NumberInput(attrs={
            'class': 'form-control',
            'min': 1,
            'max': 10
            }),
        }
