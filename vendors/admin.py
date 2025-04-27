from django.contrib import admin
from .models import Vendor
# Register your models here.

class VendorAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'store_name')
    search_fields = ('store_name',)

admin.site.register(Vendor, VendorAdmin)