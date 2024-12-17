from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """
    Модель пользователя, расширяющая стандартную модель Django.

    Поля:
    - phone_number: номер телефона пользователя.
    - date_of_birth: дата рождения пользователя.
    - created_at: дата и время создания пользователя.
    - updated_at: дата и время последнего обновления пользователя.
    """

    phone_number = models.CharField(max_length=15, **NULLABLE)
    date_of_birth = models.DateField(**NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username