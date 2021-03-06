from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from .models import Customer, Company, Address
from .forms import ProfileForm
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
        messages.success(request, "Sucessfully saved customer details")
        return HttpResponseRedirect(reverse('company'))

    context = {
        "form": form,
        "instance": instance
    }
    return render(request, 'customer/profile.html', context)


@login_required
def company(request):
    current_customer = request.user
    if (current_customer.confirmed_name is False) or (current_customer.confirmed_phone_number is False):
        return HttpResponseRedirect(reverse('profile'))

    context = {
        'current_customer': current_customer,
    }
    search_client = chwrapper.Search(settings.ACCESS_TOKEN)
    if request.method == 'POST':
        if request.POST.get('company_number'):
            query = request.POST.get('company_number')
            business_sector = request.POST.get('business_sector')
            if query:
                # business_sector = request.POST.get('business_sector')
                # print(business_sector)
                response = search_client.search_companies(query)
                response_json = response.json()
                if response_json['total_results'] == 0:
                    messages.error(request, "No results returned")
                    return render(request, 'customer/company.html', context)
                else:
                    address_dict = response_json['items'][0]['address']
                    address = Address(**address_dict)
                    address.save()
                    company = Company()
                    company.address = address
                    company.title = response_json['items'][0]['title']
                    company.company_number = response_json['items'][0]['company_number']
                    company.verified = True
                    company.business_sector = business_sector
                    company.save()
                    current_customer.company = company
                    current_customer.save()
                    context['address_dict'] = address_dict
                    context['company_number'] = company.company_number
                    context['title'] = company.title
                    messages.success(request, "Successfully confirmed company details")
                    return render(request, 'customer/company.html', context)
            else: #POST.get('company_number') empty, render regular form
                return render(request, 'customer/company.html', context)
    # request.method == 'GET':
    # query = request.GET.get("q")
        if request.POST.get('q'):
            query = request.POST.get("q")
            response = search_client.search_companies(query)
            response_json = response.json()
            companies = []
            if len(response_json['items']) == 0:
                messages.error(request, "No results returned")
                return render(request, 'customer/company.html', context)

            # for i in range(0, len(response_json['items'])):
            # total_results = response_json['total_results']
            # response = search_client.search_companies(query, items_per_page=100)
            # total_number_of_pages = (total_results // 10) + 1
            # number_per_page = 10
            # page = 1
            #for i in range((page-1)*number_per_page, page*number_per_page):
            if response_json['items'][0]['address'] is not None:
                company_address = Address(**response_json['items'][0]['address'])
            title = response_json['items'][0]['title']
            company_number = response_json['items'][0]['company_number']
            #companies.append({'company_address':company_address, 'title':title, 'company_number':company_number})

            context.update(
                {'company_address':company_address, 'title':title, 'company_number':company_number}
            )
            return render(request, 'customer/company.html', context)
    else:
        return render(request, 'customer/company.html', context)
