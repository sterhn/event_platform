from rest_framework import permissions
from users.models import UserProfile


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)
    
class IsEventPlanner(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        user_profile = UserProfile.objects.get(user=user)

        if user.is_authenticated and user_profile.role == 'event_planner':
            return True
        else:
            print(user_profile.role)
            return False