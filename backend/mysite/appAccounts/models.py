# ================================
# File: BookStore/backend/mysite/appAccounts/models.py
# ================================
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Account(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="account",
    )
    # Add any custom fields you actually need (no passwords here)
    display_name = models.CharField(max_length=120, blank=True)
    phone = models.CharField(max_length=32, blank=True)
    is_marketing_opt_in = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Account<{self.user.username}>"

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_account(sender, instance, created, **kwargs):
    # create an Account profile for every new user
    if created:
        Account.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_account(sender, instance, **kwargs):
    # keep profile in sync if needed
    if hasattr(instance, "account"):
        instance.account.save()
