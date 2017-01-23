from django.shortcuts import render
from .models import Customer

# Create your views here.
def profile(request):
    current_customer = request.user
    return render(request, 'customer/profile.html', {'current_customer':current_customer})
