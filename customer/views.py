from django.shortcuts import render
from django.conf import settings
from .models import Customer
from django.http import HttpResponse
import chwrapper

# Create your views here.
def profile(request):
    current_customer = request.user
    if request.method == 'GET':
        return render(request, 'customer/profile.html', {'current_customer':current_customer})
    elif request.method == 'POST':
        # search_term = request.POST.get("q", "")
        search_client = chwrapper.Search(settings.ACCESS_TOKEN)
        response = search_client.search_companies(request.POST.get("q", ""))
        response_json = response.json()
        if response_json['total_results'] == 0:
            return HttpResponse('No results')
        elif response_json['total_results'] > 0:
            title = response_json['items'][0]['title']
            return HttpResponse(title)
