from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from issues.models import Issue
from .serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        issue_id = self.kwargs['issue_id']
        return Comment.objects.filter(issue_id=issue_id)

    def perform_create(self, serializer):
        issue = Issue.objects.get(pk=self.kwargs['issue_id'])
        serializer.save(issue=issue, assignee=self.request.user)

        
  