from rest_framework import viewsets, permissions
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer


class IsAdminOrManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['admin', 'manager']


class IsAdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update']:
            return [IsAdminOrManager()]
        elif self.action == 'destroy':
            return [IsAdminOnly()]
        return [permissions.IsAuthenticated()]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update']:
            return [IsAdminOrManager()]
        elif self.action == 'destroy':
            return [IsAdminOnly()]
        return [permissions.IsAuthenticated()]
