from django.core.exceptions import ValidationError
from django.utils import timezone

FORBIDDEN_WORDS = ["ерунда", "глупость", "чепуха"]


def validate_age(author):
    """Проверка, что автор достиг возраста 18 лет."""
    if (
        author.date_of_birth
    ):  # Предполагается, что у пользователя есть поле date_of_birth
        age = timezone.now().year - author.date_of_birth.year
        if (timezone.now().month, timezone.now().day) < (
            author.date_of_birth.month,
            author.date_of_birth.day,
        ):
            age -= 1
        if age < 18:
            raise ValidationError("Автор поста должен быть не моложе 18 лет.")


def validate_title(value):
    """Проверка, что заголовок не содержит запрещенные слова."""
    for word in FORBIDDEN_WORDS:
        if word in value.lower():
            raise ValidationError(f"Заголовок не должен содержать слово '{word}'.")
