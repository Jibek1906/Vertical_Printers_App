from rest_framework import serializers
from .models import Printers

class PrintersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printers
        fields = '__all__'
