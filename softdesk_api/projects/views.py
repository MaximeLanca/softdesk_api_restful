from rest_framework import viewsets, generics, response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Project, Contributor
from .serializers import ProjectSerializer, ContributorSerializer, ContributorCreateSerializer
from .permissions import IsContributorOrSimpleUser
from django.db import models

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsContributorOrSimpleUser]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(models.Q(user=user) | models.Q(contributors__user=user)).distinct()

    def perform_create(self, serializer):
        project = serializer.save(user=self.request.user)
        Contributor.objects.create(user=self.request.user, project=project)
    
class ContributorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsContributorOrSimpleUser]

    def get_serializer_class(self):
        if self.action == "list":
            return ContributorSerializer  # pour lecture
        return ContributorCreateSerializer  # pour création

    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        return Contributor.objects.filter(project_id=project_id)

    def create(self, request, *args, **kwargs):
        project = Project.objects.get(pk=self.kwargs["project_id"])
        serializer = self.get_serializer(data=request.data, context={"project": project})
        serializer.is_valid(raise_exception=True)
        serializer.save(project=project)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, *args, **kwargs):
        contributor = self.get_object()
        if contributor.project.user == contributor.user:
            return Response({"detail": "Impossible de supprimer le créateur du projet."}, status=400)
        if contributor.user != contributor.project.user :
            return Response({"detail": "Impossible de supprimer ce contributeur car vous n'etes pas l'auteur du projet."}, status=400)
        contributor.delete()
        return Response({"detail":"Le contributeur a été supprimé."},status=status.HTTP_200_OK)
    
class ContributorDeleteAPIView(generics.DestroyAPIView):
    queryset = Contributor.objects.all()
    permission_classes = [IsAuthenticated]

    def delete (self, request, *args, **kwargs):
        project_id = self.kwargs["project_id"]
        contributor_id = self.kwargs["contributor_id"]

        try:
            contributor = Contributor.objects.get(id=contributor_id, project__id=project_id)

        except Contributor.DoesNotExist:
            return Response  ({"detail" : "Contributeur introuvable"}, status = status.HTTP_404_NOT_FOUND)
        
        if contributor.project.user == contributor.user :
            return Response({"detail" : "Impossible de supprimer l'auteur du projet."}, status = status.HTTP_400_BAD_REQUEST)
        
        contributor.delete()
        return Response ({"detail" : "Contributeur supprimé."}, status = status.HTTP_204_NO_CONTENT)
