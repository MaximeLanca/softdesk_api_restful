from rest_framework import serializers
from .models import Issue 

class IssueSerializer(serializers.ModelSerializer):
    class Meta():
        model = Issue
        fields = ["title","description","status","tag","project","assignee"]
        read_only_fields = ["project", "assignee"]

    def create(self, validated_data):
        return Issue.objects.create(**validated_data)
    
    