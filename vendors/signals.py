from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification
from orders.models import Order

@receiver(post_save, sender=Order)
def create_notification_for_vendor(sender, instance, created, **kwargs):
    if created:
        # Iterate through all OrderItems for the given Order
        for order_item in instance.items.all():  # Get all OrderItems associated with the order
            # Get the vendor of the product related to the OrderItem
            vendor = order_item.product.vendor  # Access the vendor of the product in the order item

            # Create the notification for the vendor
            Notification.objects.create(
                user=vendor,  # The vendor to notify
                title="New Order Received",
                message=f"A new order has been placed by {instance.customer.first_name} {instance.customer.last_name}.",
            )