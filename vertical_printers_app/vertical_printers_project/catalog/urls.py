# catalog/urls.py
from django.urls import path
from .views import PictureListView

urlpatterns = [
    path('pictures/', PictureListView.as_view(), name='picture_list'),
]
