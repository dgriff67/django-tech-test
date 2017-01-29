from django.shortcuts import render
from django.conf import settings
from .models import Loan
from customer.models import Customer
from .forms import LoanForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
@login_required
def create(request):
    current_customer = request.user
    if (current_customer.confirmed_name is False) or (current_customer.confirmed_phone_number is False):
        return HttpResponseRedirect(reverse('profile'))
    if (current_customer.profile_complete is False):
        return HttpResponseRedirect(reverse('company'))

    form = LoanForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.customer = current_customer
        instance.save()
        messages.success(request, "Successfully created loan application")
        return HttpResponse('Success')

    context = {
        'form': form,
    }
    return render(request, "loan/create.html", context)
