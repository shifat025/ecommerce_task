import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    price = django_filters.CharFilter(method='filter_price_range')
    stock = django_filters.CharFilter(method='filter_stock_range')

    class Meta:
        model = Product
        fields = ['price', 'stock']

    def filter_price_range(self, queryset, name, value):
        try:
            min_price, max_price = map(float, value.split(','))
            return queryset.filter(price__gte=min_price, price__lte=max_price)
        except ValueError:
            return queryset  # If invalid format, just return all (or you can raise an error)

    def filter_stock_range(self, queryset, name, value):
        try:
            min_stock, max_stock = map(int, value.split(','))
            return queryset.filter(stock__gte=min_stock, stock__lte=max_stock)
        except ValueError:
            return queryset