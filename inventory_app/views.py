from rest_framework import viewsets
from .models import Product, Supplier, Stock, Order
from .serializers import ProductSerializer, SupplierSerializer, StockSerializer, OrderSerializer
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# ✅ Vue landing page
def index(request):
    return render(request, 'frontend/index.html')

# ✅ ViewSets
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

# ✅ FIXED: CSRF-exempt OrderViewSet
@method_decorator(csrf_exempt, name='dispatch')
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
