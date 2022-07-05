from django.urls import path
from . import views

urlpatterns = [
    path('homeread/', views.homeread, name='homeread'),
    path('books/', views.books, name='books'),
    path('books/<int:id>', views.bookpost, name='bookpost'),
    path('loginread', views.loginread, name='loginread'),
    #path('signupread', views.signupread, name='signupread'),
    path('logout_user_read', views.logout_user_read, name='logout_user_read'),
    path('readlater', views.readlater, name='readlater'),
    path('removereadlater/<int:id>', views.removereadlater, name='removereadlater'),
    path('readhistory', views.readhistory, name='readhistory'),
    path('cread/<str:readchannel>', views.channelread, name='channelread'),
    path('uploadnovel', views.uploadnovel, name='uploadnovel'),
    path('searchnovel', views.searchnovel, name='searchnovel'),
]
