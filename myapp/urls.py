from django.urls import re_path #import url was broken
from . import views
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('',views.index_template, name='index')
]
