from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from back_api import views

urlpatterns = [
    path('test', views.test),
    path('index',views.index),
]

urlpatterns = format_suffix_patterns(urlpatterns)
