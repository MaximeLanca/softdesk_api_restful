from rest_framework.permissions import BasePermission
from .models import Contributor, Project

class IsContributorOrSimpleUser(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        project_id = view.kwargs.get('project_id')

        if not user.is_authenticated:
            return False

        if project_id is None:
            return True

        try:
            project = Project.objects.get(pk=project_id)
        except Project.DoesNotExist:
            return False

        return (
            project.user == user or
            project.contributors.filter(user=user).exists()
        )

    def has_object_permission(self, request, view, obj):
        user = request.user

        if isinstance(obj,Contributor):
            return (obj.user == user or obj.project.user == user)

        if isinstance(obj,Project):
            return (obj.user == user or obj.contributors.filter(user=user).exists())
        
        if hasattr(obj, "project"):
            return (obj.project.user == user or obj.author == user)
        
        return False