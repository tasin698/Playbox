from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.db import transaction
from .models import User, Junior, JuniorPlus, Senior


# JuniorSignUpForm extends the existing UserCreationForm
class JuniorSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    profile_pic = forms.FileField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'phone_number', 'profile_pic']

    def __init__(self, *args, **kwargs):
        super(JuniorSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_junior = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        junior = Junior.objects.create(user=user)
        junior.phone_number = self.cleaned_data.get('phone_number')
        junior.email = self.cleaned_data.get('email')
        junior.profile_pic = self.cleaned_data.get('profile_pic')
        junior.save()
        return user

# JuniorPlusSignUpForm extends the existing UserCreationForm
class JuniorPlusSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    profile_pic = forms.FileField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'phone_number', 'profile_pic']

    def __init__(self, *args, **kwargs):
        super(JuniorPlusSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_juniorplus = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        juniorplus = JuniorPlus.objects.create(user=user)
        juniorplus.phone_number = self.cleaned_data.get('phone_number')
        juniorplus.email = self.cleaned_data.get('email')
        juniorplus.profile_pic = self.cleaned_data.get('profile_pic')
        juniorplus.save()
        return user


# SeniorSignUpForm extends the existing UserCreationForm
class SeniorSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    profile_pic = forms.FileField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'phone_number', 'profile_pic']

    def __init__(self, *args, **kwargs):
        super(SeniorSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_senior = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        senior = Senior.objects.create(user=user)
        senior.phone_number = self.cleaned_data.get('phone_number')
        senior.email = self.cleaned_data.get('email')
        senior.profile_pic = self.cleaned_data.get('profile_pic')
        senior.save()
        return user


# Form to edit user profile details
class EditUserProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
