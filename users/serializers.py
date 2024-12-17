from rest_framework import serializers
from django.contrib.auth import get_user_model
from .validators import validate_password, validate_email

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели пользователя.

    Поля:
    - id: уникальный идентификатор пользователя.
    - username: имя пользователя.
    - email: адрес электронной почты пользователя.
    - phone_number: номер телефона пользователя.
    - date_of_birth: дата рождения пользователя.
    - password: пароль пользователя (только для записи).
    """

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'date_of_birth', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'validators': [validate_password]},
            'email': {'validators': [validate_email]},
        }

    def create(self, validated_data):
        """
        Создает нового пользователя с заданными данными.

        :param validated_data: данные для создания пользователя.
        :return: созданный объект пользователя.
        """
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
