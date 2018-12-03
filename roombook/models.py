from django.db import models


class Room(models.Model):
    room_number = models.CharField(max_length=200, null=True, default="")
    vacant = models.BooleanField(default=True, null=True)
    vacant_date = models.DateField(null=True, default='2008-01-01')

    def __str__(self):
        return str(Room.id)


class Book(models.Model):
    name = models.CharField(max_length=500)
    no_of_rooms = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField(max_length=500, default="okay")
    approve = models.BooleanField(default=False, null=True)
    status = models.CharField(max_length=500, default="Pending")