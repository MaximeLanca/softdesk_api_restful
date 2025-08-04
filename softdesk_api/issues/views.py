from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Issue
from projects.models import Project
from .serializers import IssueSerializer
from projects.permission import IsContributorOrSimpleUser
from django.db import models

class IssueViewSet(viewsets.ModelViewSet):
    """
    viewsets.ModelViewSet -> donne les actions automatiques (GET, POST, etc.)
    permission_classes -> Empêche les utilisateurs non connectés d'agir
    À chaque action (GET, PUT, DELETE…) sur un objet individuel, DRF appel les lignes ci-dessous
    pour permission_classes -> Si une permission retourne False → 403 Forbidden, sinon on continue.

    self.kwargs['project_id'] contient la valeur <project_id> capturée dans l’URL.
            Sert à préparer les données disponibles


    serializer.save() appelle:
                Issue.objects.create(
                title="Bug login",
                description="Erreur 500",
                project=project,
                assignee=request.user)
    """
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsContributorOrSimpleUser]

    def get_queryset(self):
        user=self.request.user
        project_id = self.kwargs['project_id']
        return Issue.objects.filter(project_id=project_id).filter(
            models.Q(project__user=user) | models.Q(project__contributors__user=user)).distinct()

    def perform_create(self, serializer):
        project = Project.objects.get(pk=self.kwargs['project_id'])
        serializer.context['project'] = project
        serializer.save(project=project, assignee=self.request.user)

    