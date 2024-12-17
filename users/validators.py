from django.core.exceptions import ValidationError
import re


def validate_password(value):
    """
    Валидатор для пароля.

    Пароль должен содержать не менее 8 символов и включать хотя бы одну цифру.

    :param value: значение пароля.
    :raises ValidationError: если пароль не соответствует требованиям.
    """
    if len(value) < 8 or not re.search(r'\d', value):
        raise ValidationError("Пароль должен содержать не менее 8 символов и включать цифры.")


def validate_email(value):
    """
    Валидатор для адреса электронной почты.

    Разрешены только домены: mail.ru, yandex.ru.

    :param value: значение адреса электронной почты.
    :raises ValidationError: если домен не разрешен.
    """
    allowed_domains = ['mail.ru', 'yandex.ru']
    if not any(value.endswith(domain) for domain in allowed_domains):
        raise ValidationError("Разрешены только домены: mail.ru, yandex.ru.")
