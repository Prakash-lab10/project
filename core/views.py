from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, LikePost, FollowersCount
from itertools import chain
import random

# Create your views here.

# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message, Comment, Like

@login_required
def feed(request):
    messages = Message.objects.all()
    return render(request, 'feed.html', {'messages': messages})

@login_required
def create_message(request):
    if request.method == 'POST':
        content = request.POST['content']
        Message.objects.create(user=request.user, content=content)
    return redirect('feed')

@login_required
def create_comment(request, message_id):
    if request.method == 'POST':
        content = request.POST['content']
        message = Message.objects.get(pk=message_id)
        Comment.objects.create(user=request.user, message=message, content=content)
    return redirect('feed')

@login_required
def like_message(request, message_id):
    message = Message.objects.get(pk=message_id)
    Like.objects.create(user=request.user, message=message)
    return redirect('feed')

@login_required
def delete_message(request, message_id):
    message = Message.objects.get(pk=message_id)
    if request.user == message.user:
        message.delete()
    return redirect('feed')
