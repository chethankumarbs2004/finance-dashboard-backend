from rest_framework.permissions import BasePermission

class RolePermission(BasePermission):
    def has_permission(self, request, view):
        allowed_roles = getattr(view, 'allowed_roles', [])
        return request.user.role in allowed_roles