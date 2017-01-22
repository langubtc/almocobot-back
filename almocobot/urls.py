from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^places$', views.PlaceList.as_view()),
    url(r'^places/(?P<pk>[0-9]+)/$', views.PlaceDetail.as_view()),
    url(r'^users$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^user_place$', views.UserPlaceList.as_view()),
    url(r'^user_place/(?P<pk>[0-9]+)/$', views.UserPlaceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)