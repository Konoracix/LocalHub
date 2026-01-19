from rest_framework import serializers
from Location.models import Location
from User.serializers.mixin_serializer import TimeStampsMixinSerializer

class LocationSerializer(TimeStampsMixinSerializer, serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'latitude', 'longitude', 'name', 'city', 'country', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']