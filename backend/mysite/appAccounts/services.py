from typing import Mapping, Any
from django.core.validators import validate_email
from django.core.exceptions import ValidationError as DJValidationError
from .factory import UserFactory

def create_user_from_payload(payload: Mapping[str, Any]):
    """
    Validates a generic payload and delegates to the factory.
    Expected keys: role (optional, default 'customer'), username, email, password, extra (dict, optional).
    """
    role = str(payload.get("role", "customer"))
    username = str(payload.get("username", "")).strip()
    email = str(payload.get("email", "")).strip().lower()
    password = str(payload.get("password", ""))

    if not username:
        raise ValueError("username is required")
    try:
        validate_email(email)
    except DJValidationError as e:
        raise ValueError(f"invalid email: {e}") from e
    if len(password) < 8:
        raise ValueError("password must be at least 8 characters")

    extra = payload.get("extra") or {}
    if not isinstance(extra, dict):
        raise ValueError("extra must be a dict if provided")
    return UserFactory.create(role, username=username, email=email, password=password, **extra)


# =============================================================================
# File: backend/mysite/appAccounts/management/commands/create_user_role.py
# Usage:
#   python manage.py create_user_role --role admin --username alice --email a@ex.com --password 'Secret123!'
# =============================================================================
from django.core.management.base import BaseCommand, CommandError
from appAccounts.services import create_user_from_payload

class Command(BaseCommand):
    help = "Create a user by role via the factory."

    def add_arguments(self, parser):
        parser.add_argument("--role", default="customer", choices=["customer", "staff", "admin"])
        parser.add_argument("--username", required=True)
        parser.add_argument("--email", required=True)
        parser.add_argument("--password", required=True)
        parser.add_argument("--first_name", default=None)
        parser.add_argument("--last_name", default=None)

    def handle(self, *args, **opts):
        payload = {
            "role": opts["role"],
            "username": opts["username"],
            "email": opts["email"],
            "password": opts["password"],
            "extra": {
                "first_name": opts.get("first_name"),
                "last_name": opts.get("last_name"),
            },
        }
        payload["extra"] = {k: v for k, v in payload["extra"].items() if v is not None}
        try:
            user = create_user_from_payload(payload)
        except Exception as e:
            raise CommandError(str(e))
        self.stdout.write(self.style.SUCCESS(f"Created {opts['role']} user: {user.id} / {user.username}"))


# =============================================================================
# File: backend/mysite/appAccounts/api.py  (optional DRF usage)
# =============================================================================
from rest_framework import serializers, views, status
from rest_framework.response import Response
from .services import create_user_from_payload

class SignupSerializer(serializers.Serializer):
    role = serializers.ChoiceField(choices=("customer", "staff", "admin"), default="customer")
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)

    def create(self, validated_data):
        role = validated_data.pop("role", "customer")
        extra = {k: v for k, v in validated_data.items() if k in ("first_name", "last_name")}
        payload = {"role": role, "extra": extra, **validated_data}
        return create_user_from_payload(payload)

class SignupView(views.APIView):
    def post(self, request):
        ser = SignupSerializer(data=request.data)
        if ser.is_valid():
            user = ser.save()
            return Response({"id": user.id, "username": user.username}, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)