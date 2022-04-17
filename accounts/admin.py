from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .form import JuniorSignUpForm, JuniorPlusSignUpForm, SeniorSignUpForm
from .models import User, Junior, JuniorPlus, Senior
from django.contrib.auth.models import Group


class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'email', 'is_junior','is_juniorplus', 'is_senior', 'is_staff']
    list_filter = ('date_joined',)


class CustomJuniorAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'email', 'phone_number']

class CustomJuniorPlusAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'email', 'phone_number']

class CustomSeniorAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'email', 'phone_number']


admin.site.site_header = 'PLAYBOX Admin Dashboard'
admin.site.register(User, CustomUserAdmin)
admin.site.register(Junior, CustomJuniorAdmin)
admin.site.register(JuniorPlus, CustomJuniorPlusAdmin)
admin.site.register(Senior, CustomSeniorAdmin)

admin.site.unregister(Group)
