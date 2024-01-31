from rest_framework import serializers

from apps.models import Class


class FullNetworkSerializer(serializers.Serializer):
    class Meta:
        fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'
