from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from issues.models import Issue
from .serializers import CommentSerializer
from projects.permission import IsContributorOrSimpleUser
from django.db import models

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsContributorOrSimpleUser]

    def get_queryset(self):
        user=self.request.user
        issue_id = self.kwargs['issue_id']
        return Comment.objects.filter(issue_id=issue_id).filter(
            models.Q(issue__project__user=user) | models.Q(issue__project_contributors__user=user)).distinct()

    def perform_create(self, serializer):
        issue = Issue.objects.get(pk=self.kwargs['issue_id'])
        serializer.save(issue=issue, assignee=self.request.user)

        
  