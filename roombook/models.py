from django.db import models


class Room(models.Model):
    vacant = models.BooleanField(default=True, null=True)

    def __str__(self):
        return str(Room.id)


class Book(models.Model):
    name = models.CharField(max_length=500)
    no_of_rooms = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField(max_length=500)
    approve = models.BooleanField(default=False, null=True)
