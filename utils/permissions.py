from rest_framework.permissions import SAFE_METHODS, BasePermission


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


class IsCustumerReadOnlyPermisson(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_superuser
