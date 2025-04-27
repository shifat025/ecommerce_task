from products.serializers import ProductSerializer
from products.models import Product
from rest_framework import serializers
from .models import OrderItem, Order

class VendorOrderItemDetailSerializer(serializers.ModelSerializer):
    product_id = serializers.SerializerMethodField()
    product_name = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['product_id', 'product_name', 'quantity', 'price']

    def get_product_id(self, obj):
        return obj.product.first().id if obj.product.exists() else None

    def get_product_name(self, obj):
        return obj.product.first().name if obj.product.exists() else None



class VendorOrderSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    customer_name = serializers.SerializerMethodField()
    customer_email = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'customer_name','customer_email','delivery_address', 'status', 'payment_status', 'total_amount', 'created_at', 'items']

    def get_items(self, obj):
        request = self.context.get('request')
        vendor = request.user.vendor_profile.first()
        # Important fix: check if vendor exists
        if not vendor:
            return []
        
        # filter order items under this vendor
        order_items = obj.items.filter(product__vendor=vendor)
        return VendorOrderItemDetailSerializer(order_items, many=True).data

    def get_customer_name(self, obj):
        return f"{obj.customer.first_name} {obj.customer.last_name}"

    def get_customer_email(self, obj):
        return obj.customer.email


class OrderItemSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField( source='product', queryset=Product.objects.all(),write_only=True)

    class Meta:
        model = OrderItem
        fields = ['product_id',  'quantity', 'price']
        read_only_fields = ['price']




class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
 
    class Meta:
        model = Order
        fields = ['id','customer',  'status', 'delivery_address', 'payment_method', 'payment_status', 'total_amount', 'items' ]
        read_only_fields = ['id','customer', 'payment_status','payment_method', 'payment_status', 'status', 'total_amount']

    def create(self, validated_data):
        items_data = validated_data.pop('items')

        order = Order.objects.create( **validated_data)
        
        total = 0
        for item_data in items_data:
            try:
                product = item_data['product']
            except Product.DoesNotExist:
                raise serializers.ValidationError(f"Product with id {item_data['product']} does not exist.")
            
            if product.stock < item_data['quantity']:
                raise serializers.ValidationError(f"Not enogh stock for {product.name}")
            
            product.stock -= item_data['quantity']
            product.save()

            order_item=OrderItem.objects.create(
                quantity=item_data['quantity'],
                price=product.price
            )

             # Now add the product properly
            order_item.product.add(product)

            # Add this order_item to the order
            order.items.add(order_item)



            total += product.price * item_data['quantity']

        order.total_amount = total
        order.save()
        return order

   