from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import AddressForm
from .models import Address, Business
from django.views.generic.edit import CreateView

# Create your views here.

def index(request):
    return HttpResponse("<h1> This is the main section</h1>")

class AddressCreate(CreateView):
    model = Address
    fields = ['address_line_1', 'address_line_2', 'postal_code', 'locality', 'region']
    success_url = '/main/business/'

class BusinessCreate(CreateView):
    model = Business
    fields = ['contact', 'name', 'registered_address', 'company_number', 'business_sector']
    success_url = '/thanks/'

def create_address(request):
    if not request.user.is_authenticated():
        return redirect('account_login')
    else:
        form = AddressForm(request.POST or None)
        if form.is_valid():
            address = form.save(commit=False)
            address.save()
            address_id = address.pk
            return redirect('business', address_id = address_id)
        context = {
            "form": form,
        }
        return render(request, 'address_form.html', context)


def create_business(request):
    if not request.user.is_authenticated():
        return redirect('account_login')
    else:
        form = BusinessForm(request.POST or None)
        if form.is_valid():
            business = form.save(commit=False)
            business.save()
            return redirect('/success/')
        context = {
            "form": form,
        }
        return render(request, 'business_form.html', context)
