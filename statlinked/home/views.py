from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from money.models import *
import datetime


def index(request):
    logged_in = "0"
    if request.user.is_authenticated:
        logged_in = "1"
    return render(request, 'home/home.html', {'logged_in' : logged_in})


def user_login(request):
    if request.method == 'POST':
        x = dict(request.POST)
        user = authenticate(username=x['email'][0], password=x['password'][0])
        if user is not None:
            login(request, user)
            return redirect('home:hub')
        else:
            return render(request, 'home/user_login.html')
    else:
        if request.user.is_authenticated:
            return redirect('home:hub')
        return render(request, 'home/user_login.html')


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home:index')


def hub(request):
    if request.user.is_authenticated:
        return render(request, 'home/hub.html')
    return redirect('home:user_login')


def register(request):
    if request.method == 'POST':
        x = dict(request.POST)\
        username = x['username'][0]
        email = x['email'][0]
        first = x['first'][0]
        last = x['last'][0]
        password = x['password'][0]
        error = 0
        if len(username) == 0 or len(first) == 0 or len(last) == 0 or len(password) == 0:
            error = 1
        try:
            User.objects.get(email=email)
            error = 1
        except User.DoesNotExist:
            pass
        try:
            User.objects.get(username=username)
            error = 1
        except User.DoesNotExist:
            pass
        if error:
            return render(request, 'home/register.html')
        user = User.objects.create_user(username, email, password)
        user.last_name = last
        user.first_name = first
        user.save()
        # ru = RegisteredUser()
        # ru.email = email
        # ru.user_id = user.id
        # ru.save()
        ud = UserData()
        datetm = datetime.datetime.now()
        ud.user_id = user
        ud.t_date = datetime.date(datetm.year, datetm.month, datetm.day)
        ud.save()

        return redirect('home:user_login')
    else:
        return render(request, 'home/register.html')
