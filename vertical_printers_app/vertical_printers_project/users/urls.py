from django.urls import path
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('users/register/', UserViewSet.as_view({'post': 'register'}), name='user-register'),
]

urlpatterns += router.urls
