from rest_framework import serializers
from .models import Eavesdropper

class EavesdropperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eavesdropper
        fields = "__all__"
