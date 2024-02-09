from django.urls import path
from apps.core.views.dashboard_views import *
from apps.core.views.deportistas.deportistas_views import *

app_name='core'
urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='Dashboard'),
    path('deportistas/list/', DeportistasListView.as_view(), name="Deportistas_list"),
    path('gracias/', gracias.as_view(), name='gracias')
]