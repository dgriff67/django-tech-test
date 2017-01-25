from django.shortcuts import render
from django.conf import settings
from .models import Customer
from django.http import HttpResponse
import chwrapper

# Create your views here.
def profile(request):
    current_customer = request.user
    query = request.GET.get("q")
    if query:
        # search_term = request.POST.get("q", "")
        search_client = chwrapper.Search(settings.ACCESS_TOKEN)
        response = search_client.search_companies(query)
        response_json = response.json()
        if response_json['total_results'] == 0:
            message = 'No results'
            return render(request, 'customer/profile.html', {'current_customer':current_customer, 'message': message})
        elif response_json['total_results'] > 0:
            company_number = response_json['items'][0]['company_number']
            title = response_json['items'][0]['title']
            address_dict = response_json['items'][0]['address']
            return render(request, 'customer/profile.html', {'current_customer':current_customer, 'company_number': company_number, 'title': title, 'address_dict': address_dict})

    else:
        return render(request, 'customer/profile.html', {'current_customer':current_customer})
