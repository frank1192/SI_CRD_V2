from django.urls import path
from django.contrib.auth.views import LogoutView
from apps.login.views import LoginFormView
from apps.login.views import *
app_name='inicio'
urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
