from rest_framework.permissions import BasePermission
from .models import Contributor, Project

class IsContributorOrSimpleUser(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        user = request.user

        if isinstance(obj,Contributor):
            return obj.user == user

        if isinstance(obj,Project):
            return (obj.user == user or obj.contributors.filter(user=user).exists())
        
        if hasattr(obj, "project"):
            return (obj.project.user == user or obj.project.contributors.filter(user=user).exists())
        
        return False