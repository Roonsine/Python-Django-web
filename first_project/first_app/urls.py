from django.conf.urls import url
from first_app import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
]