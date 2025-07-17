from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta():
        model = Project
        fields=("id","title", "user", "time_created")
    
    def create(self, validated_data):
        return Project.objects.create(**validated_data)
    
