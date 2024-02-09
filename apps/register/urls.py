from django.urls import path
from apps.register.views.RegistroDeportistas_view import *

app_name='registro'
urlpatterns = [
    path('deportistas/', CreateDeportista.as_view(), name='creardeportista')
]