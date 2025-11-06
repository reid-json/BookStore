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
