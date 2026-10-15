from rest_framework import serializers
from .models import OccupiedDate, Room, RoomImage, User
from django.contrib.auth.hashers import make_password


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['id', 'image', 'caption']

class RoomSerializer(serializers.ModelSerializer):
    images = RoomImageSerializer(many = True, read_only = True)
    class Meta:
        model = Room
        fields = ['url', 'id', 'name', 'type',
                  'pricePerNight', 'currency',
                  'maxOccupancy', 'description','images']

class OccupiedDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OccupiedDate
        fields = ['id', 'room', 'date']

