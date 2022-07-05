from django.urls import path
from . import views


urlpatterns = [
    #web app view
    path('junior_register/', views.junior_register.as_view(),name='junior_register'),
    path('juniorplus_register/', views.juniorplus_register.as_view(),name='juniorplus_register'),
    path('senior_register/', views.senior_register.as_view(),name='senior_register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('changepass/', views.user_change_pass, name='changepass'),
    path('update_profile/', views.user_profile_update, name='updateprofile'),
]

