from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('verify/', TokenVerifyView.as_view()),

    path('user/', views.UserView.as_view(), name='user'), 

    # Post List
    path('posts/', views.PostListCreateView.as_view(), name='post_list_create'),

    # Create Post
    path('post/', views.PostDetailView.as_view(), name='post_create'),

    # Retrieve, Update, and Delete a Post
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
]

