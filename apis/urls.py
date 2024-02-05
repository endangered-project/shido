from django.urls import path
from .views import *

urlpatterns = [
    path('class', get_class, name='api_get_all_class'),
    path('property_type', get_property_type_from_class, name='api_get_property_type_from_class'),
    path('instance', get_instance_from_class, name='api_get_instance_from_class'),
    path('instance/<int:instance_id>', get_instance, name='api_get_instance'),
    path('instance/random_from_class', get_random_instance_from_class, name='api_get_random_instance_from_class')
]