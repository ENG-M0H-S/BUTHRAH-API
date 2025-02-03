from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'admin'

class IsFarmerUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'farmer'

class IsRegularUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'user'