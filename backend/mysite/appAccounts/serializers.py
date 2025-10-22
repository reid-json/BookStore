from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    class Meta:
        model = User
        fields = ("username", "email", "password")

    def validate_username(self, v):
        if User.objects.filter(username__iexact=v).exists():
            raise serializers.ValidationError("Username already taken.")
        return v

    def validate_email(self, v):
        if v and User.objects.filter(email__iexact=v).exists():
            raise serializers.ValidationError("Email already registered.")
        return v

    def create(self, validated_data):
        # Critical: use create_user to hash password
        return User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            password=validated_data["password"],
            is_active=True,
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "is_staff", "is_superuser")