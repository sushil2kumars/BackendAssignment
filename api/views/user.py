from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import  logout
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics, permissions, status

from api.serializers import UserSerializer
from api.models import User


class UserView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    # Specify the queryset for this view
    queryset = User.objects.all()
    
    # Specify the serializer to use for serialization and deserialization
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]

    def get_permission_classes(self):
        if self.request.method == 'POST':
            # Allow anonymous users for the POST method for creting new user
            return [permissions.AllowAny()]
        else:
            # Require authentication for other HTTP methods (GET, PUT, DELETE)
            return [permissions.IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        # Add the User
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            hashed_password = make_password(request.data.get("password"))
            user.password = hashed_password
            user.save()
            return Response({'detail': 'Account created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        # Retrieve a specific User instance

        if request.user.is_authenticated:
            # User is authenticated, return user data
            user = request.user
            serializer = UserSerializer(user)
            data = serializer.data
        else:
            # User is not authenticated, return JSON data indicating not authenticated
            data = {'detail': 'Authentication required'}

        return Response(data)

    def update(self, request, *args, **kwargs):
        # Update user
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'User profile updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        # delete User instance
        user = request.user
        user.delete()
        # Optionally, you can log the user out here if they were logged in.
        logout(request)
        return Response({'detail': 'User deleted'}, status=status.HTTP_204_NO_CONTENT)
