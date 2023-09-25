from rest_framework import permissions

class GoalPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user_id == request.user.id

class TaskPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.goal.user_id == request.user.id

class If_thenPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.task.goal.user_id == request.user.id