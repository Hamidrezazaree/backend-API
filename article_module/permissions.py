from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)

class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or  # GET --> READ ONLY
            request.user and request.user.is_staff
        )
class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(
            request.user.is_authenticated and
            request.user.is_superuser or
            obj.author == request.user
        )

class IsSuperUserOrStaffReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
                request.method in SAFE_METHODS and
                request.user.is_staff and
                request.user or
                request.user and
                request.user.is_superuser
        )