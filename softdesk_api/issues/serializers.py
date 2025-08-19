from rest_framework import serializers
from .models import Issue 
from projects.models import Project, Contributor

class IssueSerializer(serializers.ModelSerializer):
    class Meta():
        model = Issue
        fields = ["id","title","description","status","tag","project","assignee","author","created_time"]
        read_only_fields = ["id","project","author","created_time"]

    def create(self, validated_data):
        return Issue.objects.create(**validated_data)
    
    def validate(self, attrs):
        """
        Vérifie que l'assignee fait partie des contributeurs du projet.
        """
        project = self.context.get("project")
        assignee = attrs.get("assignee")

        if assignee:
            is_contrib = Contributor.objects.filter(project=project, user=assignee).exists()

            if not (assignee == project.user or is_contrib):
                raise serializers.ValidationError({"assignee":"Cet utilisateur n'est pas contributeur de ce projet"})
        
        return attrs