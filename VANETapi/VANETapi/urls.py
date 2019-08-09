from django.contrib import admin
from django.urls import path, include
from Simulation import views as sim_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eavesdroppers/', include('Eavesdropper.urls', namespace='Eavesdropper')),
    path('simulations/', include('Simulation.urls', namespace='Simulation')),
    path('messages/', include('Message.urls', namespace='Message'))
]
