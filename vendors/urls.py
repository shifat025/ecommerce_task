from django.urls import path,include
from .views import VendorRegisterView,AllVendorView,GetVendorView
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('register/', VendorRegisterView.as_view(), name='vendor_register' ),
    path('all/', AllVendorView.as_view(), name='get_all' ),
    path('get/', GetVendorView.as_view(), name='get_single' ),
]
