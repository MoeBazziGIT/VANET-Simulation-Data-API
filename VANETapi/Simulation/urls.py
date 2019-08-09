from django.urls import path, include
from .views import add_simulation
from rest_framework import routers

app_name = 'Simulation'

urlpatterns = [
    path('', add_simulation, name='add_simulation'),
]
