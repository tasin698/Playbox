from django.db import models
from django.contrib.auth.models import AbstractUser
# added this line and settings.AUTH_USER_MODEL,
from django.conf import settings

# Custom User Model Extending AbstractUser
class User(AbstractUser):
    is_junior = models.BooleanField(default=False)
    is_juniorplus = models.BooleanField(default=False)
    is_senior = models.BooleanField(default=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


# junior Model
class Junior(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True,  related_name='junior')
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=50)
    profile_pic = models.ImageField(null=True, blank=True)
    def __str__(self):
        return str(self.user)


# juniorplus Model
class JuniorPlus(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, related_name='juniorplus')
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=50)
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.user)

# senior Model
class Senior(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, related_name='senior')
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=50)
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.user)
