# ================================
# File: BookStore/backend/mysite/appAccounts/serializers.py
# ================================
from django.contrib.auth.models import User  # default auth_user
from rest_framework import serializers
from .models import Account

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    # optional profile fields sent from frontend
    display_name = serializers.CharField(write_only=True, required=False, allow_blank=True)
    phone = serializers.CharField(write_only=True, required=False, allow_blank=True)
    is_marketing_opt_in = serializers.BooleanField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password",
                  "display_name", "phone", "is_marketing_opt_in")

    def validate_username(self, v):
        if User.objects.filter(username__iexact=v).exists():
            raise serializers.ValidationError("Username already taken.")
        return v

    def validate_email(self, v):
        if v and User.objects.filter(email__iexact=v).exists():
            raise serializers.ValidationError("Email already registered.")
        return v

    def create(self, validated_data):
        # pop profile fields before creating auth_user
        display_name = validated_data.pop("display_name", "")
        phone = validated_data.pop("phone", "")
        is_marketing_opt_in = validated_data.pop("is_marketing_opt_in", False)

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            password=validated_data["password"],
            is_active=True,
        )
        # update the related Account created by signal
        acc: Account = user.account
        acc.display_name = display_name
        acc.phone = phone
        acc.is_marketing_opt_in = is_marketing_opt_in
        acc.save(update_fields=["display_name", "phone", "is_marketing_opt_in"])
        return user

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("display_name", "phone", "is_marketing_opt_in", "created_at")

class UserMeSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    class Meta:
        model = User
        fields = ("id", "username", "email", "is_staff", "is_superuser", "account")
