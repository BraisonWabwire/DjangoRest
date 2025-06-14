from django.db.models import Max
from django.shortcuts import get_object_or_404
from .serializer import ProductSerializer,OrderSerializer,OrderItemSerialzer,productInfoSerializer
from .models import Product,Order,OrderItem
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def product_list(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_detail(request,pk):
    product=get_object_or_404(Product, pk=pk)
    serializer=ProductSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
def order_list(request):
    orders=Order.objects.all()
    serializer=OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_info(request):
    products=Product.objects.all()
    serializer= productInfoSerializer({
        'products':products,
        'count':len(products),
        'max_price':products.aggregate(max_price=Max('price'))['max_price']
        
    })
    return Response(serializer.data)
