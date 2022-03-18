from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


# Во всех классах прописана проверка на суперюзера

class IsWaiter(permissions.BasePermission):
    """Является ли сотрудник Waiter"""

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.is_superuser:
            return True
        return bool(request.user and request.user.staff.get_rank == 2)


class IsWaiterOrReadOnly(permissions.BasePermission):
    """Является ли сотрудник Waiter. Доступ к безопасным методам имеют авторизованные пользователи"""

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.is_superuser:
            return True
        return bool((request.user and request.user.get_rank == 2) or (request.method in SAFE_METHODS and
                                                                      request.user and
                                                                      request.user.is_authenticated) or (
                            request.user and request.user.is_superuser))


class IsCook(permissions.BasePermission):
    """Является ли сотрудник Cook"""

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.is_superuser:
            return True
        return bool(request.user and request.user.staff.get_rank == 1 or (
                request.user and request.user.is_superuser))


class IsAuthenticatedReadOnly(permissions.BasePermission):
    """Доступ к чтению для авторизованных пользователей"""

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return bool((request.method in SAFE_METHODS and request.user and request.user.is_authenticated) or
                    (request.user and request.user.is_superuser))
