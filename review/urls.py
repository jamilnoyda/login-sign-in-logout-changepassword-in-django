from django.conf.urls import url,include

from . import *
from . import views
from django.views.generic.base import TemplateView
app_name='review'
urlpatterns = [
    

    url(r'^signup/', views.SignUp.as_view(), name='signup'),
    url(r'^customerlist/', views.CustomerListView.as_view(), name='list'),
    #url(r'^home/', views.new, name='home'),
    





]
