from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.profile, name='profile'),
    # url(r'^(?P<q>[0-9]+)$', views.search, name='search'),
]
