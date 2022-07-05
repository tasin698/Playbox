from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('songs/', views.songs, name='songs'),
    path('rocksongs/', views.rocksongs, name='rocksongs'),
    path('popsongs/', views.popsongs, name='popsongs'),
    path('classicalsongs/', views.classicalsongs, name='classicalsongs'),
    path('songs/<int:id>', views.songpost, name='songpost'),
    path('login', views.login, name='login'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('listenlater', views.listenlater, name='listenlater'),
    path('removelistenlater/<int:id>', views.removelistenlater, name='removelistenlater'),
    
    path('favourites', views.favourites, name='favourites'),
    path('removefavourites/<int:id>', views.removefavourites, name='removefavourites'),


    path('history', views.history, name='history'),
    path('c/<str:channel>', views.channel, name='channel'),
    path('upload', views.upload, name='upload'),
    path('search', views.search, name='search'),
]
