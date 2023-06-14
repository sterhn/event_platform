from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)
    
class IsEventPlanner(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the "event_planner" role
        return request.user.profile.role == 'event_planner'