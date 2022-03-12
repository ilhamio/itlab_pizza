from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsStaffOrReadOnly(permissions.BasePermission):
    """Permission checks if user is staff"""

    def has_permission(self, request, view):
        return bool((request.method in SAFE_METHODS and
                     request.user and
                     request.user.is_authenticated) or (request.user and request.user.is_staff))