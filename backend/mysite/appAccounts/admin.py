# ================================
# File: BookStore/backend/mysite/appAccounts/admin.py
# ================================
from django.contrib import admin
from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("user", "display_name", "phone", "created_at")
    search_fields = ("user__username", "user__email", "display_name", "phone")
