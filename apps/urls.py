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
    path('instance/create/', instance_create, name='apps_instance_create'),
    path('instance_instance_connection/', instance_instance_connection_list, name='apps_instance_instance_connection_list'),
    path('instance_instance_connection/create/', instance_instance_connection_create, name='apps_instance_instance_connection_create'),
    path('instance_instance_connection/<int:instance_instance_connection_id>/', instance_instance_connection_detail, name='apps_instance_instance_connection_detail'),
]