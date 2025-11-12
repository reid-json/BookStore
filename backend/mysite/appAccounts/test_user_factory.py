import pytest
from django.contrib.auth import get_user_model
from AA_FactoryPattern_UserCreation.FactoryMulti import FactoryMulti, UnknownRoleError

pytestmark = pytest.mark.django_db
User = get_user_model()

def test_create_customer():
    user = FactoryMulti.create_user(
        role="customer",
        username="c1",
        email="c1@e.com",
        password="Passw0rd!"
    )
    assert user.is_superuser is False
    assert user.is_staff is False

def test_create_admin():
    user = FactoryMulti.create_user(
        role="admin",
        username="a1",
        email="a1@e.com",
        password="Passw0rd!"
    )
    assert user.is_superuser is True
    assert user.is_staff is True

def test_unknown_role():
    with pytest.raises(UnknownRoleError):
        FactoryMulti.create_user(
            role="nope",
            username="x",
            email="x@e.com",
            password="Passw0rd!"
        )