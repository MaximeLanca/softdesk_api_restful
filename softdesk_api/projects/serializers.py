from rest_framework import serializers
from .models import Project, Contributor

class ProjectSerializer(serializers.ModelSerializer):
    class Meta():
        model = Project
        fields=("id","title","project_type","user","created_time")
        read_only_fields = ['id', 'user']
    def create(self, validated_data):
        return Project.objects.create(**validated_data)
    
class ContributorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source = 'user.username',read_only=True)
    class Meta():
        model = Contributor
        fields=("id","user","username","project")
        read_only_fields = ["id","user","username","project"]

class ContributorCreateSerializer(serializers.ModelSerializer):
    class Meta():
        model = Contributor
        fields = ['user']
    def validate_user(self,value):
        project = self.context["project"]
        if Contributor.objects.filter(user=value, project=project).exists():
            raise serializers.ValidationError("Cet utilisateur est déjà contributeur.")
        return value