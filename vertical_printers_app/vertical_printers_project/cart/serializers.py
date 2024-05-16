from rest_framework import serializers
from .models import CartItem 
from django.contrib.auth import get_user_model
from printers import models
from django.shortcuts import get_object_or_404
User = get_user_model()

class CartItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')
    printer = serializers.ReadOnlyField(source='printer.name')
    price = serializers.ReadOnlyField(source='printer.price')

    class Meta:
        model = CartItem
        fields = "__all__"
    
class CartItemAddSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')
    printer_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CartItem
        fields = ('id', 'owner','quantity', 'printer_id', 'total_price',)
        extra_kwargs = {
            'quantity': {'required': True},
            'printer_id': {'required': True},
        }

    def create(self, validated_data):
        user = User.objects.get(id=self.context['request'].user.id)
        printer = get_object_or_404(models.Printers, id=validated_data['printer_id'])
        if printer.quantity == 0:
            raise serializers.ValidationError(
                {'Not available': 'The printer is not available.'})
        elif printer.quantity < validated_data['quantity']:
            raise serializers.ValidationError(
                {'Not available': f'Total printers at the moment:({printer.quantity})!'})

        cart_item = CartItem.objects.create(
            printer=printer,
            user=user,
            quantity=validated_data['quantity']
            )
        cart_item.save()
        cart_item.add_amount()
        printer.quantity -= cart_item.quantity
        printer.save()
        return cart_item