from django import forms
from django.contrib.auth.models import User

from .models import Address, Business, Loan

class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ['address_line_1', 'address_line_2', 'postal_code', 'locality', 'region']


class BusinessForm(forms.ModelForm):
    contact = None

    class Meta:
        model = Business
        fields = ['name', 'registered_address', 'company_number', 'business_sector']
