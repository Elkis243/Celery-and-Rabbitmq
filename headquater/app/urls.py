from django.urls import path
from .views import *

urlpatterns = [
   path('', app, name='app')
]