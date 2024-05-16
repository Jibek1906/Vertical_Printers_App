from django.urls import path, include
from rest_framework import routers
from .views import PrintersViewSet

router = routers.DefaultRouter()
router.register(r'printers', PrintersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
