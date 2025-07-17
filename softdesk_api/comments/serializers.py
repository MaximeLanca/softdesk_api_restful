from rest_framework import serializers
from .models import Comment 

class CommentSerializer(serializers.ModelSerializer):
    class Meta():
        model = Comment
        fields = ["title","description","issue","user"]

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
    
    