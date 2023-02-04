from rest_framework import serializers
from orders.models import Order, OrderItem
from customers.models import Address, Profile

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['item', 'quantity']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        exclude = ['profile', 'id', 'created_at', 'is_deleted']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    address = AddressSerializer(many=False)
    class Meta:
        model = Order
        fields = ['price', 'address', 'status', 'items']

class ProfileSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True)
    addresses = AddressSerializer(many=True)
    class Meta:
        model = Profile
        fields = ['orders', 'addresses', 'wishlist']