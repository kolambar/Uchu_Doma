from rest_framework import permissions


class IsStaffOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Проверяем, является ли пользователь сотрудником (is_staff)
        if request.user.is_staff:
            return True

        # Проверяем, является ли пользователь владельцем курса
        return obj.owner == request.user


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        # Проверяем, является ли пользователь владельцем курса
        return obj.owner == request.user
