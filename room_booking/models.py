from django.db import models

# Create your models here.

class Room(models.Model):
    ROOM_TYPES = [
        ('suite','Suite'),
        ('standard','Standart Room'),
        ('deluxe','Deluxe Room'),
    ]

    CURRENCY_TYPE = [
        ('USD', "USD"),
        ('EUR', "EUR"),
        ('BDT', "BDT"),
    ]

    name = models.CharField(max_length=100, blank = True, default='')
    type = models.CharField(max_length=100, choices = ROOM_TYPES)
    pricePerNight = models.DecimalField(max_digits=10, decimal_places=2, default=150.00)
    currency = models.CharField(max_length=10, choices = CURRENCY_TYPE, default = 'BDT')
    maxOccupancy = models.IntegerField(default=1)
    description = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name} ({self.type})"

