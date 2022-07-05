from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.shortcuts import redirect, render,  HttpResponseRedirect
from django.contrib import messages
from django.views.generic import CreateView
from .form import JuniorSignUpForm, JuniorPlusSignUpForm, SeniorSignUpForm, EditUserProfileForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .models import User




# Web app views

# Signup view for junior
class junior_register(CreateView):
    model = User
    form_class = JuniorSignUpForm
    template_name = '../templates/junior_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/accounts/profile/')


# Signup view for juniorplus
class juniorplus_register(CreateView):
    model = User
    form_class = JuniorPlusSignUpForm
    template_name = '../templates/juniorplus_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/accounts/profile/')

# Signup view for senior
class senior_register(CreateView):
    model = User
    form_class = SeniorSignUpForm
    template_name = '../templates/senior_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/accounts/profile/')


# login view
def login_request(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data.get('username')
                upass = form.cleaned_data.get('password')
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return HttpResponseRedirect('/accounts/profile/')
                else:
                    messages.error(request, "Invalid username or password")
            else:
                messages.error(request, "Invalid username or password")
        else:
            form = AuthenticationForm()
        return render(request, '../templates/login.html', context={'form': AuthenticationForm()})
    else:
        return HttpResponseRedirect('/accounts/profile/')


# profile view
def user_profile(request):
    if request.user.is_authenticated:
        account_type = "Junior" if request.user.is_junior else "JuniorPlus" if request.user.is_juniorplus else "Senior" if request.user.is_senior else "Admin"
        userprofile = {'name': request.user.username, 'first_name': request.user.first_name,
                       'last_name': request.user.last_name, 'email': request.user.email, 'account_type': account_type}
        return render(request, '../templates/profile.html', context=userprofile)
    else:
        return HttpResponseRedirect('/accounts/login/')


# logout view
def logout_view(request):
    logout(request)
    return redirect('/')


# Update Password with old Password
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password Changed Successfully!!!')
                return HttpResponseRedirect('/accounts/profile/')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, '../templates/changepass.html', {'form': form})
    else:
        return HttpResponseRedirect('/accounts/login/')


# User profile update view
def user_profile_update(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = EditUserProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Profile Updated !!!')
                form.save()
                return HttpResponseRedirect('/accounts/profile/')
        else:
            form = EditUserProfileForm(instance=request.user)
        return render(request, '../templates/updateprofile.html', {'name': request.user, 'form': form})
    else:
        return HttpResponseRedirect('/accounts/login/')
