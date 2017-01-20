from django.shortcuts import render
from .models import Customer

# Create your views here.
def profile(request):
    current_customer = request.user
    data_dict = {'username':current_customer.username}
    return render(request, 'customer/profile.html', data_dict)
