# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return '%s' % (self.title)

class Mood(models.Model):
    status = models.CharField(max_length=10, null=False)
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return '%s' % (self.status)

class Talk(models.Model):
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10, default='不願意透漏身分的人')
    message = models.TextField(null=False)
    del_pass = models.CharField(max_length=10)
    pub_time = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.message)
