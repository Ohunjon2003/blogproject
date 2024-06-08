from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, LikeToggle
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

urlpatterns = [
    path('posts/<int:post_id>/like/', LikeToggle.as_view(), name='like-toggle'),
    path('', include(router.urls)),
    path('auth/', obtain_auth_token, name='auth'),
    path('register/', UserCreate.as_view(), name='register'),
]
