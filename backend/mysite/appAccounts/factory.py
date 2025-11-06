from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol, Dict, Any, TypeVar
from django.contrib.auth import get_user_model, password_validation
from django.core.exceptions import ValidationError as DJValidationError
from django.db import transaction, IntegrityError

User = get_user_model()
TUser = TypeVar("TUser")

class BaseUserCreator(Protocol):
    """
    Strategy interface for role-specific user creation.
    """

    def create(self, *, username: str, email: str, password: str, **extra: Any) -> TUser: ...


@dataclass(frozen=True)
class AdminCreator:
    """
    Creates a superuser using Django's built-in manager.
    """

    def create(self, *, username: str, email: str, password: str, **extra: Any) -> User:
        password_validation.validate_password(password)
        with transaction.atomic():
            return User.objects.create_superuser(username=username, email=email, password=password)


@dataclass(frozen=True)
class StaffCreator:
    """
    Creates a staff (non-superuser) account.
    """

    def create(self, *, username: str, email: str, password: str, **extra: Any) -> User:
        password_validation.validate_password(password)
        with transaction.atomic():
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_staff = True
            # Apply whitelisted extras to avoid mass assignment
            for k, v in extra.items():
                if hasattr(user, k):
                    setattr(user, k, v)
            user.full_clean(validate_unique=False)
            user.save()
            return user


@dataclass(frozen=True)
class CustomerCreator:
    """
    Creates a normal customer account.
    """

    def create(self, *, username: str, email: str, password: str, **extra: Any) -> User:
        password_validation.validate_password(password)
        with transaction.atomic():
            user = User.objects.create_user(username=username, email=email, password=password)
            for k, v in extra.items():
                if hasattr(user, k):
                    setattr(user, k, v)
            user.full_clean(validate_unique=False)
            user.save()
            return user


class UnknownRoleError(ValueError):
    """Raised when an unknown role is requested."""


class UserFactory:
    """
    Registry-based factory for creating users by role.
    """

    _creators: Dict[str, BaseUserCreator] = {}

    @classmethod
    def register(cls, role: str, creator: BaseUserCreator) -> None:
        key = role.strip().lower()
        if key in cls._creators:
            raise ValueError(f"Creator already registered for role '{role}'")
        cls._creators[key] = creator

    @classmethod
    def replace(cls, role: str, creator: BaseUserCreator) -> None:
        cls._creators[role.strip().lower()] = creator

    @classmethod
    def create(cls, role: str, *, username: str, email: str, password: str, **extra: Any) -> User:
        key = role.strip().lower()
        creator = cls._creators.get(key)
        if not creator:
            raise UnknownRoleError(f"Unknown role '{role}'. Registered roles: {list(cls._creators)}")
        try:
            return creator.create(username=username, email=email, password=password, **extra)
        except (DJValidationError, IntegrityError) as e:
            raise ValueError(f"Failed to create {role}: {e}") from e


# Default roles
UserFactory.register("admin", AdminCreator())
UserFactory.register("staff", StaffCreator())
UserFactory.register("customer", CustomerCreator())