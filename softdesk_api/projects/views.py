from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Project
from .serializers import ProjectSerializer
from .permission import IsContributorOrSimpleUser
from django.db import models

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsContributorOrSimpleUser]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(models.Q(user=user) | models.Q(contributors__user=user)).distinct()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
