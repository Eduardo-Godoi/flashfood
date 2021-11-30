from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsCustumerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return not request.user.is_superuser


class IsPartnerPermisson(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_superuser
