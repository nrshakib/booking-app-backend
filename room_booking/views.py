from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from .models import Room, RoomImage
from .serializers import RoomImageSerializer, RoomSerializer

# Create your views here.
@api_view(['get'])
def api_root(request, format = None):
    return Response({
        'rooms': reverse('room_list', request = request, format = format)
    })

class RoomImageUploadMixin:
    def save_uploaded_images(self, room):
        images = self.request.FILES.getlist('images')
        caption = self.request.data.get('caption', '')

        for image in images:
            RoomImage.objects.create(
                room=room,
                image=image,
                caption=caption
            )

class RoomList(generics.ListCreateAPIView, RoomImageUploadMixin):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def perform_create(self, serializer):
        room = serializer.save()
        self.save_uploaded_images(room)



class RoomDetail(generics.RetrieveUpdateDestroyAPIView, RoomImageUploadMixin):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def perform_update(self, serializer):
        room = serializer.save()
        self.save_uploaded_images(room)