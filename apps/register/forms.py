from django.forms import *
from django import forms

from apps.register.models import Deportistas

class DeportistasForm(ModelForm):
    class Meta:
        model= Deportistas
        fields= '__all__'
        widgets = {
            'codigo': TextInput(
                attrs={
                    'placeholder': 'Ingrese un codigo',
                }
            ),
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese su nombre',
                }
            ),
            'cedula': TextInput(
                attrs={
                    'placeholder': 'ingrese su cedula',
                }
            ),
            'apellidos': TextInput(
                attrs={
                    'placeholder': 'ingrese sus apellidos',
                }
            ),
            'fecha_nacimiento': TextInput(
                attrs={
                    'placeholder': 'ingrese su fecha de nacimiento',
                }
            ),
            'genero': TextInput(
                attrs={
                    'placeholder': 'ingrese su genero',
                }
            ),
            'altura': TextInput(
                attrs={
                    'placeholder': 'ingrese su altura',
                }
            ),
            'peso': TextInput(
                attrs={
                    'placeholder': 'ingrese su peso',
                }
            ),
            'talla_camisa': TextInput(
                attrs={
                    'placeholder': 'ingrese su talla de camisa',
                }
            ),
            'talla_pantalon': TextInput(
                attrs={
                    'placeholder': 'ingrese su talla de pantalon',
                }
            ),
            'fecha_vinculacion': TextInput(
                attrs={
                    'placeholder': 'ingrese cuando se unio al equipo',
                }
            ),
            'promedio_total_acomulado': TextInput(
                attrs={
                    'placeholder': 'ingrese su promedio total acomulado',
                }
            ),
            'Estamento': Select(
                attrs={
                    'class': 'select2',
                }
            ),
            'SeleccionadoDeportivo': Select(
                attrs={
                    'class': 'select2',
                }
            )
            
        }