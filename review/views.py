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

def new(request):
    if request.method == "POST":
        form = forms.AccountForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.instance.user = self.request.user

            post.save()
            return redirect('accounts/home')

            
    else:
        form = forms.AccountForm()
    return render(request, 'accounts/account_edit.html', {'form': form})