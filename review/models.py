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


class Customer(models.Model):
  company = models.ForeignKey(User, default=1)
  customer_first_name = models.CharField(null=False, blank=False, max_length=50)
  customer_last_name = models.CharField(null=False, blank=False, max_length=50)
  customer_email = models.CharField(null=False, blank=False, max_length=80)
  account_number = models.CharField(null=False, blank=False, max_length=20)
  address1 = models.CharField(null=False, blank=False, max_length=50)
  address2 = models.CharField(null=False, blank=False, max_length=20)
  city = models.CharField(null=False, blank=False, max_length=50)
  state = models.CharField(null=False, blank=False, max_length=2)
  customer_email = models.CharField(null=False, blank=False, max_length=80)
  primary_phone = models.CharField(null=False, blank=False, max_length=12)
  
