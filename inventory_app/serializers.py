from rest_framework import serializers
from .models import Product, Supplier, Stock, Order, OrderItem

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        exclude = ['order']  # ✅ Don't ask for 'order' field in API request

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'date', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

            # Update stock
            stock = Stock.objects.get(product=item_data['product'])
            if stock.quantity < item_data['quantity']:
                raise serializers.ValidationError(
                    f"Not enough stock for {item_data['product'].name}"
                )
            stock.quantity -= item_data['quantity']
            stock.save()

        return order
