from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2000)
    director = models.CharField(max_length=2000)
    tags = models.CharField(max_length=100)
    image = models.CharField(max_length=100000, default="")
    movie = models.FileField(upload_to='movie')
    description = models.CharField(max_length=1000, default="")
    is_junior_movie = models.BooleanField(default=False)
    is_juniorplus_movie = models.BooleanField(default=False)
    is_senior_movie = models.BooleanField(default=False)
    is_action_movie = models.BooleanField(default=False)
    is_thriller_movie = models.BooleanField(default=False)
    is_comedy_movie = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Watchlater(models.Model):
    watch_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    watch_video_id = models.CharField(max_length=10000000, default="")

    def __str__(self):
        return self.name

class WatchFavourites(models.Model):
    wfavourites_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fvideo_id = models.CharField(max_length=10000000, default="")

    def __str__(self):
        return self.name


class WatchHistory(models.Model):
    hist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=10000000, default="")

    def __str__(self):
        return self.name

class WatchChannel(models.Model):
    watch_channel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    video = models.CharField(max_length=100000000)

    def __str__(self):
        return self.name
