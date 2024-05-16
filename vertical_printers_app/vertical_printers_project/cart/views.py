from rest_framework import permissions, filters, generics, response

from django.shortcuts import get_object_or_404
from .serializers import CartItemSerializer, CartItemAddSerializer, CartItem
from .models import Printers



class CartItemView(generics.ListAPIView):
    serializer_class = CartItemSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = [filters.SearchFilter]

    def get_queryset(self):
        user = self.request.user
        return CartItem.objects.filter(user=user)



class CartItemAddView(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemAddSerializer
    permission_classes = (permissions.AllowAny,)


class CartItemDeleteView(generics.DestroyAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = CartItem.objects.all()


    def delete(self, request, pk, format=None):
        user = request.user
        cart_item = CartItem.objects.filter(user=user)
        target_printer = get_object_or_404(cart_item, pk=pk)
        printer = get_object_or_404(Printers, id=target_printer.printers.id)
        printer.quantity = printer.quantity + target_printer.quantity
        printer.save()
        target_printer.delete()
        return response.Response(data={"detail": "deleted"}, status=200)