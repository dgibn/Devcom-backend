from rest_framework import serializers
from mainapp.models import bookings
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=bookings
        fields="__all__"