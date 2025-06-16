from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, SupplierViewSet, StockViewSet, OrderViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('suppliers', SupplierViewSet)
router.register('stocks', StockViewSet)
router.register('orders', OrderViewSet)

urlpatterns = router.urls
