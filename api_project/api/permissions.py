from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Allow all users to read, but restrict modifying to admin users only
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user.is_staff
