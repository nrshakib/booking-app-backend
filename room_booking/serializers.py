from rest_framework import serializers
from .models import Room, RoomImage

class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['id', 'image', 'caption']

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    images = RoomImageSerializer(many = True, read_only = True)
    class Meta:
        model = Room
        fields = ['url', 'id', 'name', 'type',
                  'pricePerNight', 'currency',
                  'maxOccupancy', 'description','images']