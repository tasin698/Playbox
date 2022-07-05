from django.urls import path
from . import views

urlpatterns = [
    path('homewatch/', views.homewatch, name='homewatch'),
    path('movies/', views.movies, name='movies'),
    path('actionmovies/', views.actionmovies, name='actionmovies'),
    path('thrillermovies/', views.thrillermovies, name='thrillermovies'),
    path('comedymovies/', views.comedymovies, name='comedymovies'),
    path('movies/<int:id>', views.moviepost, name='moviepost'),
    path('loginwatch', views.loginwatch, name='loginwatch'),
    path('logout_user_watch', views.logout_user_watch, name='logout_user_watch'),
    path('watchlater', views.watchlater, name='watchlater'),
    path('removewatchlater/<int:id>', views.removewatchlater, name='removewatchlater'),
    path('watchhistory', views.watchhistory, name='watchhistory'),

    path('wfavourites', views.wfavourites, name='wfavourites'),
    path('removewfavourites/<int:id>', views.removewfavourites, name='removewfavourites'),

    path('cwatch/<str:watchchannel>', views.channelwatch, name='channelwatch'),
    path('uploadvideo', views.uploadvideo, name='uploadvideo'),
    path('searchvideo', views.searchvideo, name='searchvideo'),
]
