from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^registrations$', views.registrations, name='registrations'),
    url(r'^units$', views.units, name='units'),
]
