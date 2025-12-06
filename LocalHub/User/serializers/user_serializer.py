from rest_framework import serializers
from User.serializers.mixin_serializer import LocationMixinSerializer, TimeStampesMixinSerializer
from User.models import User

class UserSerializer(LocationMixinSerializer, TimeStampesMixinSerializer, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'bio', 'birth_date', 'gender', 'is_veryfied', 'first_name', 'last_name', 'latitude', 'longitude', 'location_name', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']