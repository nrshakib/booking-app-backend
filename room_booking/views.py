from django.shortcuts import render
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Room
from .serializers import RoomSerializer

# Create your views here.
@api_view(['get'])
def api_root(request, format = None):
    return Response({
        'rooms': reverse('room_list', request = request, format = format)
    })


class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
