from typing import Dict, Any
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError as DJValidationError
from django.db import IntegrityError
from .FactoryInterface import AbstractUserFactory
from .FactoryConcrete import AdminUserFactory, CustomerUserFactory

User = get_user_model()

class UnknownRoleError(ValueError):
    """Raised when an unknown role is requested."""

class FactoryMulti:
    _factories: Dict[str, AbstractUserFactory] = {}

    @classmethod
    def register(cls, role: str, factory: AbstractUserFactory) -> None:
        key = role.strip().lower()
        if key in cls._factories:
            raise ValueError(f"Factory already registered for role '{role}'")
        cls._factories[key] = factory

    @classmethod
    def replace(cls, role: str, factory: AbstractUserFactory) -> None:
        cls._factories[role.strip().lower()] = factory

    @classmethod
    def create_user(cls, role: str, *, username: str, email: str, password: str, **extra: Any) -> User:
        key = role.strip().lower()
        factory = cls._factories.get(key)
        if not factory:
            raise UnknownRoleError(f"Unknown role '{role}'. Registered roles: {list(cls._factories)}")
        try:
            return factory.create_user(username=username, email=email, password=password, **extra)
        except (DJValidationError, IntegrityError) as e:
            raise ValueError(f"Failed to create {role}: {e}") from e

# Register factories
FactoryMulti.register("admin", AdminUserFactory())
FactoryMulti.register("customer", CustomerUserFactory())