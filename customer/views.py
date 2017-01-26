from django.shortcuts import render
from django.conf import settings
from .models import Customer, Company
from .forms import ProfileForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
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
        return HttpResponseRedirect(reverse('company'))

    context = {
        "form": form,
        "instance": instance
    }
    return render(request, 'customer/profile.html', context)

def company(request):
    current_customer = request.user
    context = {
        'current_customer': current_customer,
    }
    search_client = chwrapper.Search(settings.ACCESS_TOKEN)
    if request.method == 'POST':
        query = request.POST.get('company_number')
        if query:
            response = search_client.search_companies(query)
            response_json = response.json()
            if response_json['total_results'] == 0:
                # message = 'Something has gone wrong' + company_number
                return render(request, 'customer/company.html', context)
            else:
                company_dict = response_json['items'][0]['address']
                company_dict['title'] = response_json['items'][0]['title']
                company_dict['company_number'] = response_json['items'][0]['company_number']
                c = Company(**company_dict)
                c.save()
                current_customer.company = c
                current_customer.save()
                context['company_dict'] = company_dict
                # message = 'Company confirmed'
                return render(request, 'customer/company.html', context)
        else: #we just landed as POST with POST.get('company_number') empty, render regular form
            return render(request, 'customer/company.html', context)
    query = request.GET.get("q")
    if query:
        # search_term = request.POST.get("q", "")
        response = search_client.search_companies(query)
        response_json = response.json()
        if response_json['total_results'] == 0:
            message = 'No results'
            return render(request, 'customer/company.html', {'current_customer':current_customer, 'message': message})
        elif response_json['total_results'] > 0:
            company_address = response_json['items'][0]['address']
            title = response_json['items'][0]['title']
            company_number = response_json['items'][0]['company_number']
            context.update({'title': title, 'company_number': company_number, 'company_address': company_address})
            return render(request, 'customer/company.html', context)
    else:
        return render(request, 'customer/company.html', context)
