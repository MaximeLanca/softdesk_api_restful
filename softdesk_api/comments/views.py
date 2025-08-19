from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Comment
from projects.models import Project
from issues.models import Issue
from .serializers import CommentSerializer
from projects.permissions import IsContributorOrSimpleUser
from .permissions import IsCommentAuthorOrProjectContributor


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsContributorOrSimpleUser, IsCommentAuthorOrProjectContributor]

    def get_queryset(self):
        issue_id = self.kwargs['issue_id']
        return Comment.objects.filter(issue_id=issue_id).select_related("assignee")

    def create(self, request, *args, **kwargs):
        project = Project.objects.get(pk=self.kwargs["project_id"])
        issue = Issue.objects.get(pk=self.kwargs['issue_id'])
        serializer = self.get_serializer(data=request.data, context={"project": project})
        serializer.is_valid(raise_exception=True)
        serializer.save(issue=issue, author=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
  