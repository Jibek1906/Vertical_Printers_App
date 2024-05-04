from django.urls import path
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('users/register/', UserViewSet.as_view({'post': 'register'}), name='user-register'),
    path('users/<int:pk>/update_profile/', UserViewSet.as_view({'put': 'update_profile'}), name='user-update-profile'),
    path('users/<int:pk>/delete/', UserViewSet.as_view({'delete': 'delete_user'}), name='user-delete'),
    path('users/view_profile/<int:pk>/', UserViewSet.as_view({'get': 'view_profile'}), name='user-view-profile'),
]

urlpatterns += router.urls
