# catalog/views.py
from rest_framework import generics
from .models import Picture
from .serializers import PictureSerializer

class PictureListView(generics.ListAPIView):
    queryset = Picture.objects.all()  # Make sure there's no reference to the genre field here
    serializer_class = PictureSerializer
