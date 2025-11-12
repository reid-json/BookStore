from django.db.models.signals import post_save
from django.dispatch import receiver
from appOrders.models import OrdersModel
from .utils import send_email_notification

@receiver(post_save, sender=OrdersModel)
def notify_on_order_finalized(sender, instance, **kwargs):
    if instance.finalized and instance.user.email:
        subject = "Your Order Has Been Finalized"
        message = f"Hi {instance.user.username}, your order {instance.order_id} has been finalized. Thanks for shopping with us!"
        send_email_notification(instance.user.email, subject, message)
        print(f"[DEBUG] Signal triggered for order {instance.order_id}")