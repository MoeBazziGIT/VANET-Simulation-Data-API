from django.db import models

# Create your models here.
class Message(models.Model):
    sender_address = models.CharField(max_length=100)
    sender_psynm = models.IntegerField()
    sender_vel_x = models.FloatField()
    sender_vel_y = models.FloatField()
    sender_pos_x = models.FloatField()
    sender_pos_y = models.FloatField()
    sender_angle = models.FloatField()

    # simTime_sent = models.FloatField()
    # simTime_received = models.FloatField()
    simTime_eavesdropped = models.FloatField()

    # CPN_readyFlag = models.BooleanField(default=False)
    is_encrypted = models.BooleanField(default=False)
