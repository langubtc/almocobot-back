from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^places$', views.place_list),
    url(r'^places/(?P<pk>[0-9]+)/$', views.place_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)