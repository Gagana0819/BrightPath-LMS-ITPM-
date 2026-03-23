from rest_framework import permissions

class IsLecturer(permissions.BasePermission):
    """
    Custom permission to only allow lecturers to access.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'LECTURER')

class IsStudent(permissions.BasePermission):
    """
    Custom permission to only allow students to access.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'STUDENT')
