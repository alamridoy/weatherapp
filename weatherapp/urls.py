from django.urls import path
from weatherapp.views import *
urlpatterns = [
    path('',home , name='home')
]
