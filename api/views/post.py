from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Q
from api.models import Post
from api.serializers import PostSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class PostListCreateView(generics.ListCreateAPIView):
    # Specify the queryset for this view
    queryset = Post.objects.all()
    
    # Specify the serializer to use for serialization and deserialization
    serializer_class = PostSerializer
    
    # Specify the authentication classes to use for this view
    authentication_classes = [JWTAuthentication]
    
    # Specify the permission classes to determine access control
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        # Get the initial queryset
        queryset = self.get_queryset()

        # Search by title, content, or author name
        query = self.request.query_params.get('query', '')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(author__username__icontains=query)
            )

        # Sorting
        sort_by = self.request.query_params.get('sort_by', 'created_at')
        if sort_by == 'name':
            queryset = queryset.order_by('title')
        elif sort_by == 'created':
            queryset = queryset.order_by('created_at')
        else:
            queryset = queryset.order_by('-created_at')

        # Serialize the queryset and return as a response
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PostDetailView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    # Specify the queryset for this view
    queryset = Post.objects.all()
    
    # Specify the serializer to use for serialization and deserialization
    serializer_class = PostSerializer
    
    # Specify the authentication classes to use for this view
    authentication_classes = [JWTAuthentication]
    
    # Specify the permission classes to determine access control
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Add the author ID to the request data before creating the Post
        request.data['author'] = request.user.id
        
        # Create a PostSerializer instance with the request data
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            # Save the Post with the authenticated user as the author
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        # Retrieve a specific Post instance
        instance = self.get_object()
        
        # Serialize the instance and return as a response
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        # Retrieve a specific Post instance
        instance = self.get_object()
        
        # Check if the authenticated user is the author of the Post
        if instance.author != request.user:
            return Response(
                {"detail": "You don't have permission to update this post."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        # Update the Post instance with the request data
        serializer = PostSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        # Retrieve a specific Post instance
        instance = self.get_object()
        
        # Check if the authenticated user is the author of the Post
        if instance.author != request.user:
            return Response(
                {"detail": "You don't have permission to delete this post."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        # Delete the Post instance
        instance.delete()
        
        # Return a success response
        return Response(status=status.HTTP_204_NO_CONTENT)
