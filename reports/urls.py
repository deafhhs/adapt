from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^(?P<slug>[^/]+)/$', views.report_view, name='report'),
 ]