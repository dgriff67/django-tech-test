from django.contrib import admin

# Register your models here.
from .models import Customer, Company, Address

admin.site.register(Customer)
admin.site.register(Company)
admin.site.register(Address)
