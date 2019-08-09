from django.db import models
from Message.models import Message

# Create your models here.
class Simulation(models.Model):
    start_time = models.CharField(max_length=100)
    dev_name = models.CharField(max_length=100)
    privacy_scheme = models.CharField(max_length=100)
