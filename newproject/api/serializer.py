from rest_framework import serializers
from .models import Product,Order,OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=(
            'id',
            'name',
            'description',
             'price',
             'stock',
        )

        def validate_price(self,value):
            if value<=0:
                raise serializers.ValidationError(
                    'price must be greater than 0.'
                )
            return value
        
class OrderItemSerialzer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields=("product","quantity")
        
class OrderSerializer(serializers.ModelSerializer):
    items=OrderItemSerialzer(many=True, read_only=True)
    total_price=serializers.SerializerMethodField(method_name='total')

    def total(self,obj):
        order_items=obj.items.all()
        return sum(order_item.item_subtotal for order_item in order_items)

    class Meta:
        model=Order
        fields=(
            "order_id",
            "created_at",
            "user",
            "status",
            "items",
            "total_price")
        

class productInfoSerializer(serializers.Serializer):
    products=ProductSerializer(many=True)
    count=serializers.IntegerField()
    max_price=serializers.FloatField()