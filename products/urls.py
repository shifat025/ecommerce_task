from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProductViewSet, ProductPublicViewSet

router = DefaultRouter()
router.register(r'product', ProductViewSet,basename='product'),
router.register(r'allproduct', ProductPublicViewSet,basename='all_product')

urlpatterns = [
    path('', include(router.urls)),
]
