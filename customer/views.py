from django.shortcuts import render
from django.conf import settings
from .models import Customer, Company, Address
from .forms import ProfileForm, CompanyForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import chwrapper

# Create your views here.
@login_required
def profile(request):
    instance = request.user
    form = ProfileForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.confirmed_phone_number = True
        instance.confirmed_name = True
        instance.save()
        return HttpResponseRedirect(reverse('company'))

    context = {
        "form": form,
        "instance": instance
    }
    return render(request, 'customer/profile.html', context)

@login_required
def company(request):
    current_customer = request.user
    context = {
        'current_customer': current_customer,
    }
    search_client = chwrapper.Search(settings.ACCESS_TOKEN)
    if request.method == 'POST':
        query = request.POST.get('company_number')
        if query:
            # business_sector = request.POST.get('business_sector')
            # print(business_sector)
            response = search_client.search_companies(query)
            response_json = response.json()
            if response_json['total_results'] == 0:
                # message = 'Something has gone wrong' + company_number
                return render(request, 'customer/company.html', context)
            else:
                address_dict = response_json['items'][0]['address']
                address = Address(**address_dict)
                address.save()
                company = Company()
                company.address = address
                company.title = response_json['items'][0]['title']
                company.company_number = response_json['items'][0]['company_number']
                company.save()
                current_customer.company = company
                current_customer.save()
                context['address_dict'] = address_dict
                context['company_number'] = company.company_number
                context['title'] = company.title
                # message = 'Company confirmed'
                return render(request, 'customer/company.html', context)
        else: #POST.get('company_number') empty, render regular form
            return render(request, 'customer/company.html', context)
    # request.method == 'GET':
    query = request.GET.get("q")
    if query:
        response = search_client.search_companies(query)
        response_json = response.json()
        if response_json['total_results'] == 0:
            message = 'No results'
            return render(request, 'customer/company.html', context)
        elif response_json['total_results'] > 0:
            company_address = response_json['items'][0]['address']
            title = response_json['items'][0]['title']
            company_number = response_json['items'][0]['company_number']
            context.update({
                'title': title,
                'company_number': company_number,
                'company_address': company_address,
            })
            return render(request, 'customer/company.html', context)
    else:
        return render(request, 'customer/company.html', context)
