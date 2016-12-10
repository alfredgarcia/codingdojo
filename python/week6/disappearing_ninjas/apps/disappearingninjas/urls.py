from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninjas$', views.all),
    url(r'^(?P<color>\w+)/$', views.ninja)
]
