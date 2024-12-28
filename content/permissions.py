from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Разрешение, позволяющее редактировать и удалять только владельцам объекта или администраторам.
    Остальные пользователи могут только просматривать.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешить доступ на чтение для всех
        if request.method in permissions.SAFE_METHODS:
            return True
        # Разрешить доступ на запись только владельцу или администратору
        return obj.author == request.user or request.user.is_staff