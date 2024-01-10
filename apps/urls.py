from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='apps_home'),
    path('class/', class_list, name='apps_class_list'),
    path('class/<int:class_id>/', class_detail, name='apps_class_detail'),
    path('class/<int:class_id>/edit/', class_edit, name='apps_class_edit'),
    path('class/create/', class_create, name='apps_class_create'),
    path('instance/', instance_list, name='apps_instance_list'),
    path('instance/<int:instance_id>/', instance_detail, name='apps_instance_detail'),
    path('instance/<int:instance_id>/edit/', instance_edit, name='apps_instance_edit'),
    path('instance/<int:instance_id>/property/', instance_property_list, name='apps_instance_property_list'),
    path('instance/<int:instance_id>/property/<int:property_type_id>/', instance_property_form, name='apps_instance_property_form'),
    path('instance/create/', instance_create, name='apps_instance_create'),
    path('instance_instance_connection/', instance_instance_connection_list, name='apps_instance_instance_connection_list'),
    path('instance_instance_connection/create/', instance_instance_connection_create, name='apps_instance_instance_connection_create'),
    path('instance_instance_connection/<int:instance_instance_connection_id>/', instance_instance_connection_detail, name='apps_instance_instance_connection_detail'),
    path('property_type/', property_type_list, name='apps_property_type_list'),
    path('property_type/create/', property_type_create, name='apps_property_type_create'),
    path('property_type/<int:property_type_id>/', property_type_detail, name='apps_property_type_detail')
]