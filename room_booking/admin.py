from django.contrib import admin

from room_booking.models import OccupiedDate, Room, RoomImage

# Register your models here.
admin.site.register(Room)
admin.site.register(RoomImage)
admin.site.register(OccupiedDate)
