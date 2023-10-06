from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated


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


class IsAuthenticatedNoStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        # Проверяем, является ли пользователь сотрудником (is_staff)
        return bool(request.user and request.user.is_authenticated and not request.user.is_staff)

