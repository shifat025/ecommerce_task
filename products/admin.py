from django.contrib import admin
from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'vendor', 'price', 'stock')
    search_fields = ('name',)
    list_filter = ('vendor',)

admin.site.register(Product, ProductAdmin)