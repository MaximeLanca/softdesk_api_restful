from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsIssueAuthorOrProjectContributor(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if request.method in SAFE_METHODS:
            return (obj.project.user == user or
                    obj.project.contributors.filter(user=user).exists())

        return obj.author == user