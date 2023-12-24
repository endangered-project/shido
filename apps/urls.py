from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='apps_home'),
    path('class/', class_list, name='apps_class_list'),
    path('class/<int:class_id>/', class_detail, name='apps_class_detail'),
    path('class/create/', class_create, name='apps_class_create'),
    path('instance/', instance_list, name='apps_instance_list'),
    path('instance/<int:instance_id>/', instance_detail, name='apps_instance_detail'),
    path('instance/create/', instance_create, name='apps_instance_create'),
]