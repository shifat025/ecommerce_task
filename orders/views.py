from rest_framework import viewsets, pagination
from .models import Order, OrderItem
from .serializers import OrderSerializer, VendorOrderSerializer
from rest_framework.permissions import IsAuthenticated
from authentication.permissions import IsVendor, IsCustomer
from vendors.models import Vendor

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsCustomer]
    pagination_class = pagination.PageNumberPagination
    http_method_names = ['get', 'post']

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(customer=self.request.user)
    

class VendorOrderItemViewSet(viewsets.ReadOnlyModelViewSet):
    """Vendor can view their ordered products."""
    serializer_class = VendorOrderSerializer
    permission_classes = [IsAuthenticated, IsVendor]
    agination_class = pagination.PageNumberPagination
    http_method_names = ['get']

    def get_queryset(self):
        vendor = Vendor.objects.get(user=self.request.user)
        return Order.objects.filter(items__product__vendor=vendor).distinct().prefetch_related('items__product')
