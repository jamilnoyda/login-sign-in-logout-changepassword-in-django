# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from django.views import generic
from django.urls import reverse_lazy
from . import forms

from django.contrib.auth.forms import UserCreationForm


###
from django.views.generic import ListView

from django_tables2 import RequestConfig
from .models import Customer
from .tables import CustomerTable

###

# Create your views here.


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

# class AccountDetailView(generic.DetailView):
    
    
#     template_name = 'accounts/home.html'

# def new(request):
#     if request.method == "POST":
#         form = forms.AccountForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user = request.user
#             post.instance.user = self.request.user

#             post.save()
#             return redirect('accounts/home')

            
#     else:
#         form = forms.AccountForm()
#     return render(request, 'accounts/account_edit.html', {'form': form})
class CustomerListView( ListView):
  model = Customer
  template_name = 'accounts/customers.html'
  context_object_name = 'customer'
  ordering = ['id']
  

  def get_context_data(self, **kwargs):
    context = super(CustomerListView, self).get_context_data(**kwargs)
    context['nav_customer'] = True
    #table = CustomerTable(Customer.objects.filter(self.kwargs['']).order_by('-pk'))
    table = CustomerTable(Customer.objects.filter(pk=1))
    RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
    context['table'] = table
    return context