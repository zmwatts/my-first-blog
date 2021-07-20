from django.db import models
from django.utils import timezone


# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    plot_summary = models.CharField(max_length=1000)
    release_date = models.DateTimeField(default=timezone.now)
    director = models.CharField(max_length=50)