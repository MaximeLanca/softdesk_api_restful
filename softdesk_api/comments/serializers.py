from rest_framework import serializers
from .models import Comment 
from projects.models import Contributor


class CommentSerializer(serializers.ModelSerializer):
    username_author = serializers.CharField(source = 'author.username',read_only=True)
    username_assignee = serializers.CharField(source = 'assignee.username',read_only=True)

    class Meta():
        model = Comment
        fields = ["uuid","description","issue","author","username_author","assignee","username_assignee","created_time"]
        read_only_fields = ['issue','author','username_author','assignee','username_assignee','created_time']

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
    
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