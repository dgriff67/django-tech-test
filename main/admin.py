from django.contrib import admin
from .models import Address, Business, Loan

# Register your models here.
admin.site.register(Address)
admin.site.register(Business)
admin.site.register(Loan)
