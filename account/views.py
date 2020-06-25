from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

from .forms import LoginForm, UserRegistrationForm


# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])  # return user object. Verify a set of credentials.
            if user is not None:
                if user.is_active:
                    login(request, user)  # Saves the user’s ID in the session, using Django’s session framework.
                    return HttpResponse('Success authenticate!')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login or password!')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])  # User model method for saving password more secure
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        form = UserRegistrationForm()
    return render(request, 'account/register.html', {'form': form})
