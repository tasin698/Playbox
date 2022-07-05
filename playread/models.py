from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# AGE_CHOICES=(
#     ('All','All'),
#     ('junior','junior'),
#     ('juniorplus','juniorplus'),
#     ('senior','senior'),
# )

# Create your models here.

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2000)
    author = models.CharField(max_length=2000)
    tags = models.CharField(max_length=100)
    image = models.CharField(max_length=100000, default="")
    book = models.FileField(upload_to='book')
    description = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name

class Readlater(models.Model):
    read_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    read_novel_id = models.CharField(max_length=10000000, default="")

    def __str__(self):
        return self.name

class Readhistory(models.Model):
    hist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    novel_id = models.CharField(max_length=10000000, default="")

    def __str__(self):
        return self.name

class Readchannel(models.Model):
    read_channel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    novel = models.CharField(max_length=100000000)

    def __str__(self):
        return self.name
