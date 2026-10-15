from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from .models import OccupiedDate, Room, RoomImage
from .serializers import OccupiedDateSerializer, RoomSerializer

# Create your views here.
@api_view(['get'])
def api_root(request, format = None):
    return Response({
        'rooms': reverse('room_list', request = request, format = format),
        'occupied_dates': reverse(
            'occupied-date-list',
            request=request,
            format=format
        )
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

class OccupiedDateList(generics.ListCreateAPIView):
    queryset = OccupiedDate.objects.all()
    serializer_class = OccupiedDateSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser and not user.is_staff:
            return OccupiedDate.objects.filter(user = user)
        
        return super().get_queryset()

class OccupiedDateDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = OccupiedDate.objects.all()
    serializer_class = OccupiedDateSerializer
