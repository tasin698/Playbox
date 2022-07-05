from django.contrib import admin
from .models import Book, Readlater, Readhistory, Readchannel

# Register your models here.

admin.site.register(Book)
admin.site.register(Readlater)
admin.site.register(Readhistory)
admin.site.register(Readchannel)
