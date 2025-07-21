from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta():
        model = Project
        fields=("id","title", "user")
    
    def create(self, validated_data):
        return Project.objects.create(**validated_data)
    
