# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from django.views import generic
from django.urls import reverse_lazy
from . import forms

from django.contrib.auth.forms import UserCreationForm


# Create your views here.


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

# class AccountDetailView(generic.DetailView):
    
    
#     template_name = 'accounts/home.html'

