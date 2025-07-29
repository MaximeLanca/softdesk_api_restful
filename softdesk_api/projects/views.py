from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Project
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # project_id = self.kwargs['pk']
        return Project.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
