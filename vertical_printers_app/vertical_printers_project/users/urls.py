from django.urls import path
from rest_framework import routers
from .views import UserViewSet
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('register/', UserViewSet.as_view({'post': 'register'}), name='user-register'),
    path('<int:pk>/update_profile/', UserViewSet.as_view({'put': 'update_profile'}), name='user-update-profile'),
    path('<int:pk>/delete/', UserViewSet.as_view({'delete': 'delete_user'}), name='user-delete'),
    path('view_profile/<int:pk>/', UserViewSet.as_view({'get': 'view_profile'}), name='user-view-profile'),
    path('list/', UserViewSet.as_view({'get': 'list_users'}), name='user-list'),
    path('info/', UserViewSet.as_view({'get': 'user_info_by_token'}), name='user-info-by-token'),
]

urlpatterns += router.urls
