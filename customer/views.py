from django.shortcuts import render
from django.conf import settings
from .models import Customer, Company
from .forms import ProfileForm
from django.http import HttpResponse
import chwrapper

# Create your views here.
def profile(request):
    instance = request.user
    form = ProfileForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.confirmed_phone_number = True
        instance.confirmed_name = True
        instance.save()

    context = {
        "form": form,
        "instance": instance
    }
    return render(request, 'customer/profile.html', context)
    """current_customer = request.user
    search_client = chwrapper.Search(settings.ACCESS_TOKEN)
    if request.method == 'GET':
        query = request.GET.get("q")
        if query:
            # search_term = request.POST.get("q", "")
            response = search_client.search_companies(query)
            response_json = response.json()
            if response_json['total_results'] == 0:
                message = 'No results'
                return render(request, 'customer/profile.html', {'current_customer':current_customer, 'message': message})
            elif response_json['total_results'] > 0:
                company_address = response_json['items'][0]['address']
                title = response_json['items'][0]['title']
                company_number = response_json['items'][0]['company_number']
                return render(request, 'customer/profile.html', {'current_customer':current_customer, 'title': title, 'company_number': company_number, 'company_address': company_address})

        else:
            # return render(request, 'customer/profile.html', {'current_customer':current_customer})
            return render(request, 'customer/profile.html', context)"""
    """else: #request.method == 'POST'
        query = request.POST.get('company_number')
        response = search_client.search_companies(query)
        response_json = response.json()
        if response_json['total_results'] == 0:
            message = 'Something has gone wrong' + company_number
            return render(request, 'customer/profile.html', {'current_customer':current_customer, 'message': message})
        else:
            company_dict = response_json['items'][0]['address']
            company_dict['title'] = response_json['items'][0]['title']
            company_dict['company_number'] = response_json['items'][0]['company_number']
            c = Company(**company_dict)
            c.save()
            current_customer.company = c
            current_customer.save()
            message = 'Company confirmed'
            return render(request, 'customer/profile.html', {'current_customer':current_customer, 'message': message, 'company_dict': company_dict})"""
