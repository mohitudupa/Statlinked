from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
import datetime
from random import randint


color = {0: 'indigo', 1: 'red', 2: 'teal', 3: 'indigo', 4: 'red', 5: 'teal'}


def index(request):
    if request.user.is_authenticated:
        x = Note.objects.filter(user_id=request.user)[::-1]
        return render(request, 'notes/home.html', {'notes': x})
    else:
        return redirect('home:user_login')


def add_note(request):
    if request.user.is_authenticated and request.method == 'POST':
        x = dict(request.POST)
        note = Note()
        cur_user = User.objects.get(id=request.user.id)
        note.user_id = cur_user
        note.title = x['title'][0][:25]
        note.body = x['body'][0][:250]
        dattim = datetime.datetime.now()
        note.written_date = datetime.date(dattim.year, dattim.month, dattim.day)
        note.color = color[randint(0, 5)]
        note.save()
        return redirect('notes:index')
    return redirect('notes:index')


def del_note(request):
    if request.user.is_authenticated and request.method == 'POST':
        x = dict(request.POST)
        note_id = int(x['action'][0]) - 1
        cur_user = User.objects.get(id=request.user.id)
        note = Note.objects.filter(user_id=cur_user)[::-1][note_id]
        note.delete()
        return redirect('notes:index')
    return redirect('notes:index')


def edit_note(request):
    if request.user.is_authenticated and request.method == 'POST':
        x = dict(request.POST)
        note_id = int(x['action'][0]) - 1
        cur_user = User.objects.get(id=request.user.id)
        note = Note.objects.filter(user_id=cur_user)[::-1][note_id]
        note.delete()
        note = Note()
        note.user_id = cur_user
        note.title = x['title'][0][:25]
        note.body = x['body'][0][:250]
        dattim = datetime.datetime.now()
        dat = datetime.date(dattim.year, dattim.month, dattim.day)
        note.written_date = dat
        note.color = color[randint(0, 5)]
        note.save()
        return redirect('notes:index')
    return redirect('notes:index')
