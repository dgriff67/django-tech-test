from django.shortcuts import render
from .models import Customer

# Create your views here.
def profile(request):
    return render(request, 'customer/profile.html', request.user)
