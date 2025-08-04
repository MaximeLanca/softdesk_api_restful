from rest_framework import serializers
from .models import Comment 

class CommentSerializer(serializers.ModelSerializer):
    class Meta():
        model = Comment
        fields = ["uuid","description","issue","author","assignee","created_time"]
        read_only_fields = ['issue',"author",'assignee']

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
    
    