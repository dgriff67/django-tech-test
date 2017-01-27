from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from customer import urls
from loan import urls

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='profile')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^profile/', include('customer.urls')),
    url(r'^loan/', include('loan.urls')),
]
