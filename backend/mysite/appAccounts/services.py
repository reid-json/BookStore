from typing import Mapping, Any
from django.core.validators import validate_email
from django.core.exceptions import ValidationError as DJValidationError
from AA_FactoryPattern_UserCreation.FactoryMulti import FactoryMulti


def create_user_from_payload(payload: Mapping[str, Any]):
    """
    Validates a generic payload and delegates to the factory.
    Expected keys: role (optional, default 'customer'), username, email, password, extra (dict, optional).
    """
    role = str(payload.get("role", "customer")).strip().lower()
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

    return FactoryMulti.create_user(
        role=role,
        username=username,
        email=email,
        password=password,
        **extra
    )