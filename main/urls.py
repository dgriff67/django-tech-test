from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^registration/$', views.create_address, name='register'),
    url(r'^business/$', views.create_business, name='business'),
]
