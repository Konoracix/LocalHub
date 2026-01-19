from rest_framework import viewsets
from User.models import User
from User.serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    def get_serializer_class(self):
        if self.action == "get_distance":
            return UserSerializer 
        return UserSerializer
    

    @action(detail=True, methods=['put'])
    def get_distance(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        user = User.objects.filter(pk=pk).first()
        serializer.is_valid()
        return Response({
            "distance": user.get_distance(serializer.validated_data['latitude'], serializer.validated_data['longitude'])
        })