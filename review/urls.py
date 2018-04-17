from django.conf.urls import url,include

from . import *
from . import views
from django.views.generic.base import TemplateView
app_name='review'
urlpatterns = [
    

    url(r'^signup/', views.SignUp.as_view(), name='signup'),
    url(r'^signup/', views.new, name='home'),





]
