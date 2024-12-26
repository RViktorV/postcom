from users.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(username="admin", email="admin@yandex.ru", date_of_birth="2000-01-01")
        user.set_password("1q2w3e4r")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

        self.stdout.write(self.style.SUCCESS("Администратор успешно создан!"))
