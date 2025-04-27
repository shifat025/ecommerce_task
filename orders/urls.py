from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, VendorOrderItemViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register('vendor-orders', VendorOrderItemViewSet, basename='vendor-orders')

urlpatterns = [
    path('', include(router.urls)),
]
