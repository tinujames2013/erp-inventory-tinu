# inventory_app/urls.py
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet, StockViewSet, SupplierViewSet

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'stocks', StockViewSet)
router.register(r'suppliers', SupplierViewSet)

urlpatterns = router.urls
