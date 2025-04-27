from django.shortcuts import render
from rest_framework import viewsets,pagination, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ProductSerializer
from .models import Product
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from authentication.permissions import IsVendor
from vendors.models import Vendor
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated,IsVendor]
    pagination_class = pagination.PageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'description']  # Search by name, description
    filterset_fields = ['price', 'stock']    # Filter by price and stock
    ordering_fields = ['price', 'created_at']  # Sort by price or created date

    def get_queryset(self):
        vendor = Vendor.objects.get(user=self.request.user)
        return Product.objects.filter(vendor=vendor)
    
    def perform_create(self, serializer):
        vendor = Vendor.objects.get(user=self.request.user)
        serializer.save(vendor=vendor)