from AA_FactoryPattern_UserCreation.FactoryInterface import AbstractUserFactory
from appAccounts.factory import User


class DefaultUserFactory(AbstractUserFactory):
    def create_user(self, username, email, password, **extra_fields):
        return User.objects.create_user(
            username=username,
            email=email,
            password=password,
            **extra_fields
        )