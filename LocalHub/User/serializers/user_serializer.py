from rest_framework import serializers
from User.serializers.mixin_serializer import TimeStampsMixinSerializer
from User.models import User
from Location.serializers import LocationSerializer

class UserSerializer(TimeStampsMixinSerializer, serializers.ModelSerializer):
    location = LocationSerializer(required=False)

    class Meta:
        model = User
        fields = ['id', 'email', 'bio', 'birth_date', 'gender', 'is_veryfied', 'first_name', 'last_name', 'location', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']