from rest_framework import serializers
from orders.models import Order, OrderItem
from customers.models import Address, Profile
from products.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'descriptions', 'picture1', 'stock', 'final_price']

class OrderItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=False)
    class Meta:
        model = OrderItem
        fields = ['item', 'quantity']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
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
    wishlist = ItemSerializer(many=True)
    class Meta:
        model = Profile
        fields = ['orders', 'addresses', 'wishlist']