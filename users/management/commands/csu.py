from users.models import User
from django.core.management import BaseCommand

import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("ADMIN_USERNAME")
email = os.getenv("ADMIN_EMAIL")
password = os.getenv("ADMIN_PASSWORD")
date_of_birth = os.getenv("ADMIN_DATE_OF_BIRTH")


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            username=username, email=email, date_of_birth=date_of_birth
        )
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

        self.stdout.write(self.style.SUCCESS("Администратор успешно создан!"))
