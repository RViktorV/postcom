from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Разрешение, позволяющее редактировать и удалять только администраторам.
    Остальные пользователи могут только просматривать.
    """

    def has_permission(self, request, view):
        # Разрешить доступ на чтение для всех
        if request.method in permissions.SAFE_METHODS:
            return True
        # Разрешить доступ на запись только администраторам
        return request.user and request.user.is_staff