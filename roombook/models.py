from django.db import models


class Room(models.Model):
    vacant = models.BooleanField(default=True)
    alloted = models.OneToOneField('Book', on_delete=models.CASCADE,)


class Book(models.Model):
    name = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    no_of_rooms = models.CharField(max_length=500)
