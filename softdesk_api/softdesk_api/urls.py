from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import DataUserAPIView, RegisterView
from projects.views import ProjectListCreateAPIView, ProjectDeleteAPIView
from issues.views import IssueListCreateAPIView
from comments.views import CommentListCreateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', DataUserAPIView.as_view()),
    path('api/signup/', RegisterView.as_view(), name='signup'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/projects/', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('api/projects/<int:pk>/', ProjectDeleteAPIView.as_view(), name='project-delete'),
    path('api/projects/<int:project_id>/issues/', IssueListCreateAPIView.as_view(), name='create_or_get_issue'),
    path('api/projects/<int:project_id>/issues/<int:issue_id>/comments', CommentListCreateAPIView.as_view(), name='crecreate_or_get_comment'),
]   
