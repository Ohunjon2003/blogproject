from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, LikeToggle, UserCreate,PostVideoViewSet
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'post-video',PostVideoViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="API documentation for Blog project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('posts/<int:post_id>/like/', LikeToggle.as_view(), name='like-toggle'),
    path('', include(router.urls)),
    path('auth/', obtain_auth_token, name='auth'),
    path('register/', UserCreate.as_view(), name='register'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
