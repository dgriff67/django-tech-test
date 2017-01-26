from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.profile, name='profile'),
    url(r'^company$', views.company, name='company'),
]
