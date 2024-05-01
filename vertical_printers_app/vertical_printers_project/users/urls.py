from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet
from django.urls import path
from .views import MyTokenObtainPairView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]