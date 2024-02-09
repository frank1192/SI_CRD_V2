from django.urls import path

from apps.login.views import LoginFormView
from apps.login.views import *

urlpatterns = [
    path('', LoginFormView, name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
