from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class UserCreateView(generics.CreateAPIView):
    """
    Представление для регистрации новых пользователей.

    Этот класс позволяет создавать новых пользователей. При успешной
    регистрации возвращает данные о пользователе и токены доступа
    (refresh и access) для аутентификации.
    """

    queryset = User.objects.all()  # Запрос для получения всех пользователей
    permission_classes = [
        permissions.AllowAny
    ]  # Разрешаем доступ для всех пользователей
    serializer_class = UserSerializer  # Сериализатор для обработки данных регистрации

    def post(self, request, *args, **kwargs):
        """
        Обрабатывает POST-запрос для регистрации нового пользователя.

        Проверяет валидность данных, создает нового пользователя,
        генерирует токены и возвращает их в ответе.

        Args:
            request (Request): HTTP-запрос с данными для регистрации.
            *args: Дополнительные аргументы.
            **kwargs: Дополнительные именованные аргументы.

        Returns:
            Response: Ответ с данными о пользователе и токенами.
        """
        serializer = self.get_serializer(
            data=request.data
        )  # Получаем сериализатор с данными запроса
        serializer.is_valid(raise_exception=True)  # Проверяем валидность данных
        user = serializer.save()  # Сохраняем нового пользователя
        refresh = RefreshToken.for_user(
            user
        )  # Генерируем токены для нового пользователя
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,  # Данные пользователя
                "refresh": str(refresh),  # Токен refresh
                "access": str(refresh.access_token),  # Токен access
            }
        )


class UserListView(generics.ListAPIView):
    """
    Представление для получения списка всех пользователей.
    Доступно для авторизованных пользователей и администраторов.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Представление для получения, обновления или удаления конкретного пользователя.
    Доступно только для авторизованных пользователей.
    Администраторы могут управлять всеми пользователями,
    обычные пользователи могут редактировать только себя.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Возвращает queryset пользователей.
        Если пользователь - администратор, возвращает всех пользователей.
        В противном случае возвращает только текущего пользователя.
        """
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        return User.objects.filter(id=user.id)
