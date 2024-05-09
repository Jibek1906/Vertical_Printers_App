from django.urls import path, include
from rest_framework import routers
from .views import PrinterViewSet

router = routers.DefaultRouter()
router.register(r'printers', PrinterViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.CartItemView.as_view(), name="cart"),
    path('add/', views.CartItemAddView.as_view()),
    path('delete/<int:pk>/', views.CartItemDeleteView.as_view()),
]
