from rest_framework.permissions import BasePermission
from users.models import Role


class IsUserAuthenticatedPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated()


class IsSuperAdminPermission(BasePermission):
    def has_permission(self, request, view):
        return Role.ADMIN in list(map(lambda role: role.id, request.user.roles.all())) or request.user.is_superuser


class IsAdminPermission(BasePermission):
    def has_permission(self, request, view):
        return Role.ADMIN in list(map(lambda role: role.id, request.user.roles.all()))


class IsSupervisorPermission(BasePermission):
    def has_permission(self, request, view):
        return Role.SUPERVISOR in list(map(lambda role: role.id, request.user.roles.all()))


class IsSecretaryPermission(BasePermission):
    def has_permission(self, request, view):
        return Role.SECRETARY in list(map(lambda role: role.id, request.user.roles.all()))


class IsTeacherPermission(BasePermission):
    def has_permission(self, request, view):
        return Role.TEACHER in list(map(lambda role: role.id, request.user.roles.all()))


class IsStudentPermission(BasePermission):
    def has_permission(self, request, view):
        return Role.STUDENT in list(map(lambda role: role.id, request.user.roles.all()))
