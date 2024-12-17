from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from .validators import validate_password, validate_email

User  = get_user_model()

class UserCreateView(generics.CreateAPIView):
    """
    Представление для создания нового пользователя.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

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
