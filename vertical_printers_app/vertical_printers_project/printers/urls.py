from django.urls import path, include
from rest_framework import routers
from .views import PrinterViewSet

router = routers.DefaultRouter()
router.register(r'printers', PrinterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
