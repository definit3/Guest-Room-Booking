from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=500)
    roll = models.CharField(max_length=500)
    leave_start_date = models.DateField()
    leave_end_date = models.DateField()
    reason = models.CharField(max_length=500)
