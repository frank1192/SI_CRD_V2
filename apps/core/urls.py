from django.urls import path
from apps.core.views.dashboard_views import *

app_name='core'
urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='Dashboard'),
    path('gracias/', gracias.as_view(), name='gracias')
]