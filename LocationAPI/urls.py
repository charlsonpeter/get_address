from django.urls import path, re_path
from django.conf.urls import url
from .views import *
urlpatterns = [
            path('get_address/<str:lat>/<str:long>/', GetAddress.as_view())
            ]
