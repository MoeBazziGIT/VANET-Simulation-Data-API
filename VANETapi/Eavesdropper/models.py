from django.db import models
from Message.models import Message
from Simulation.models import Simulation

# Create your models here.
class Eavesdropper(models.Model):
    index = models.IntegerField()
    eavesdropped_messages = models.ManyToManyField(Message)
    simulation = models.ForeignKey(Simulation, on_delete=models.CASCADE)
