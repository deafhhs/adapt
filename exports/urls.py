from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^registrations$', views.registrations, name='registrations'),
    url(r'^units$', views.units, name='units'),
    url(r'^$', views.IndexView.as_view(template_name='exports/index.html')),
]
