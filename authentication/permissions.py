from rest_framework import permissions

class IsRole(permissions.BasePermission):
    role = None
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == self.role
    
class IsAdmin(IsRole):
    role = 'admin'

class IsVendor(IsRole):
    role = 'vendor'

class IsCustomer(IsRole):
    role = 'customer'