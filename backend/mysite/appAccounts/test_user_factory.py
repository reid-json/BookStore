import pytest
from django.contrib.auth import get_user_model
from appAccounts.factory import UserFactory, UnknownRoleError

pytestmark = pytest.mark.django_db
User = get_user_model()

def test_create_customer():
    u = UserFactory.create("customer", username="c1", email="c1@e.com", password="Passw0rd!")
    assert u.is_superuser is False and u.is_staff is False

def test_create_staff():
    u = UserFactory.create("staff", username="s1", email="s1@e.com", password="Passw0rd!")
    assert u.is_superuser is False and u.is_staff is True

def test_create_admin():
    u = UserFactory.create("admin", username="a1", email="a1@e.com", password="Passw0rd!")
    assert u.is_superuser is True and u.is_staff is True

def test_unknown_role():
    with pytest.raises(UnknownRoleError):
        UserFactory.create("nope", username="x", email="x@e.com", password="Passw0rd!")