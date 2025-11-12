from typing import Protocol, Any, TypeVar
from django.contrib.auth import get_user_model

User = get_user_model()
TUser = TypeVar("TUser")

class AbstractUserFactory(Protocol):
    def create_user(self, *, username: str, email: str, password: str, **extra: Any) -> TUser:
        ...