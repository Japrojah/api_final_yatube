from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    """Кастомный пермишн.
    Переопределены методы has_permission & has_object_permission."""

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
