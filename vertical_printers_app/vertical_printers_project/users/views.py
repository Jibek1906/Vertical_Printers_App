from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def view_profile(self, request, pk=None):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def list_users(self, request):
        queryset = self.queryset
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Generate tokens for the newly registered user
        user = serializer.instance
        refresh = Token.objects.create(user=user)

        return Response({
            'user': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.key),
        }, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['put'])
    def update_profile(self, request, pk=None):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @action(detail=True, methods=['delete'])
    def delete_user(self, request, pk=None):
        user = self.get_object()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['get'])
    def get_profile_update_form(self, request, pk=None):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    @permission_classes([IsAuthenticated])
    def user_info_by_token(self, request):
        user = request.user
        user_data = {
            'username': user.username,
            'email': user.email,
        }
        return Response(user_data)
