from rest_framework import serializers

from apps.models import Class, PropertyType, Instance, ObjectPropertyRelation


class FullNetworkSerializer(serializers.Serializer):
    class Meta:
        fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'


class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        exclude = ['class_instance']


class ObjectPropertyRelationSerializer(serializers.ModelSerializer):
    property_type = PropertyTypeSerializer()

    class Meta:
        model = ObjectPropertyRelation
        exclude = ['instance_object']


class InstanceSerializer(serializers.ModelSerializer):
    property_values = serializers.SerializerMethodField()

    class Meta:
        model = Instance
        exclude = ['class_instance']

    def get_property_values(self, obj):
        return ObjectPropertyRelationSerializer(ObjectPropertyRelation.objects.filter(instance_object=obj), many=True).data
