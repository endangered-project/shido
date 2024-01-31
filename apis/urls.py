from django.urls import path
from .views import *

urlpatterns = [
    path('class', get_all_class, name='api_get_all_class')
]