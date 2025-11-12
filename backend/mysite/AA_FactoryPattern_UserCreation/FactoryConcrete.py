from dataclasses import dataclass
from django.contrib.auth import get_user_model, password_validation
from django.db import transaction
from typing import Any
from .FactoryInterface import AbstractUserFactory

User = get_user_model()

@dataclass(frozen=True)
class AdminUserFactory(AbstractUserFactory):
    def create_user(self, *, username: str, email: str, password: str, **extra: Any) -> User:
        password_validation.validate_password(password)
        with transaction.atomic():
            return User.objects.create_superuser(username=username, email=email, password=password)

@dataclass(frozen=True)
class CustomerUserFactory(AbstractUserFactory):
    def create_user(self, *, username: str, email: str, password: str, **extra: Any) -> User:
        password_validation.validate_password(password)
        with transaction.atomic():
            user = User.objects.create_user(username=username, email=email, password=password)
            for k, v in extra.items():
                if hasattr(user, k):
                    setattr(user, k, v)
            user.full_clean(validate_unique=False)
            user.save()
            return user