# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from datetime import datetime
from django.shortcuts import redirect

# Create your views here.

def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')

def talking(request):
    template = get_template('talking.html')

    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = models.Mood.objects.all()

    try:
        urid = request.GET['user_id']
        urpass = request.GET['user_pass']
        user_talk = request.GET['user_talk']
        user_mood = request.GET['user_mood']
    except:
        urid = None
        message = '如要張貼訊息，則每一個欄位都要填 ...'

    if user_id != None:
        mood = models.Mood.objects.get(status=user_mood)
        talk = models.Post.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_talk)
        talk.save()
        message='成功储存!請記得你的編輯密碼[{}]!，訊息需經審查後才會顯示。'.format(user_pass)

    html = template.render.get(locals())

    return HttpResponse(html)
