from django.contrib import admin
from .models import *


admin.site.register(Class)
admin.site.register(Instance)
admin.site.register(InstanceInstanceConnection)
admin.site.register(InstanceInstanceRelation)
admin.site.register(PropertyType)
admin.site.register(ObjectPropertyRelation)