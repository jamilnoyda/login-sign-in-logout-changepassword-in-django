# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Account(models.Model):
    name = models.TextField()
    number = models.IntegerField(blank=True, null=True)
    city = models.TextField(default="")
    pin = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField()