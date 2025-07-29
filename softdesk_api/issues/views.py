from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Issue
from projects.models import Project
from .serializers import IssueSerializer

class IssueViewSet(viewsets.ModelViewSet):
    """
    viewsets.ModelViewSet -> donne les actions automatiques (GET, POST, etc.)
    permission_classes -> Empêche les utilisateurs non connectés d'agir
    """
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """self.kwargs['project_id'] contient la valeur <project_id> capturée dans l’URL."""
        project_id = self.kwargs['project_id']
        return Issue.objects.filter(project_id=project_id)

    def perform_create(self, serializer):
        project = Project.objects.get(pk=self.kwargs['project_id'])
        serializer.save(project=project, assignee=self.request.user)

    