import django_tables2 as tables
from django_tables2.utils import A

from django.contrib.auth.models import User




class CustomerTable(tables.Table):
  
    customer_user_name = tables.LinkColumn('customer-detail', args=[A('pk')])
  
    customer_email = tables.LinkColumn('customer-detail', args=[A('pk')])
    class Meta:
        model = User
        fields = '__all__'
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There are no customers matching the search criteria..."