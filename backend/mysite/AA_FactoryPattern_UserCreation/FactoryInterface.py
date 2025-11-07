from abc import ABC, abstractmethod
from django.contrib.auth.models import User

class AbstractUserFactory(ABC):
    @abstractmethod
    def create_user(self, username, email, password, **extra_fields):
        pass