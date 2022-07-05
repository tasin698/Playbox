from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2000)
    singer = models.CharField(max_length=2000)
    tags = models.CharField(max_length=100)
    image = models.CharField(max_length=100000, default="")
    song = models.FileField(upload_to='song')
    movie = models.CharField(max_length=1000, default="")
    is_junior_song = models.BooleanField(default=False)
    is_juniorplus_song = models.BooleanField(default=False)
    is_senior_song = models.BooleanField(default=False)
    is_classical_song = models.BooleanField(default=False)
    is_rock_song = models.BooleanField(default=False)
    is_pop_song = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Listenlater(models.Model):
    listen_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    listen_music_id = models.CharField(max_length=10000000, default="")

    def __str__(self):
        return self.name


class Favourites(models.Model):
    favourites_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fmusic_id = models.CharField(max_length=10000000, default="")

    def __str__(self):
        return self.name

class History(models.Model):
    hist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    music_id = models.CharField(max_length=10000000, default="")

    def __str__(self):
        return self.name

class Channel(models.Model):
    channel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    music = models.CharField(max_length=100000000)

    def __str__(self):
        return self.name
