from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Issue
from .serializers import IssueSerializer

class IssueListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, project_id):
        issues = Issue.objects.filter(project__id=project_id)
        serializer = IssueSerializer(issues, many=True)
        return Response(serializer.data)

    def post(self, request, project_id):
        data = request.data.copy()
        data['project'] = project_id 
        serializer = IssueSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    