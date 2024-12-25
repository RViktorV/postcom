from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешение, позволяющее редактировать и удалять только владельцам объекта.
    Остальные пользователи могут только просматривать.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешить доступ на чтение для всех
        if request.method in permissions.SAFE_METHODS:
            return True
        # Разрешить доступ на запись только владельцу
        return obj.author == request.user