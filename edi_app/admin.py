from django.contrib import admin

from django.contrib import admin
from .models import EDIMessage,  Customer, Supplier, Product

admin.site.register(EDIMessage)
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Product)