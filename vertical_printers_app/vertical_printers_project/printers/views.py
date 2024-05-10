from rest_framework import viewsets
from .models import Printers
from .serializers import PrintersSerializer
from rest_framework import permissions

class PrintersViewSet(viewsets.ModelViewSet):
    queryset = Printers.objects.all()
    serializer_class = PrintersSerializer

    def get_permissions(self):
        return permissions.IsAuthenticated(),