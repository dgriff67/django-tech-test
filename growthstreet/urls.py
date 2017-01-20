from django.conf.urls import include, url
from django.contrib import admin
from customer import urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^profile/', include('customer.urls')),
]
