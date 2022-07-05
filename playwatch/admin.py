from django.contrib import admin
from .models import Movie, Watchlater, WatchChannel, WatchHistory

# Register your models here.

admin.site.register(Movie)
admin.site.register(Watchlater)
admin.site.register(WatchChannel)
admin.site.register(WatchHistory)
