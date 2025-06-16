from rest_framework import viewsets
from .models import Product, Supplier, Stock, Order
from .serializers import ProductSerializer, SupplierSerializer, StockSerializer, OrderSerializer

from django.shortcuts import render

def frontend(request):
    return render(request, 'index.html')  # this should point to dist/index.html

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
