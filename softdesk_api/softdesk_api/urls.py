from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import RegisterView
from projects.views import ProjectViewSet, ContributorViewSet
from issues.views import IssueViewSet
from comments.views import CommentViewSet

issue_list_create = IssueViewSet.as_view({
    'get':'list',
    'post':'create'
    })

issue_detail = IssueViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update'
    })

comment_list_create = CommentViewSet.as_view({
    'get':'list',
    'post':'create',
})

comment_detail = CommentViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update'
})

project_list_create = ProjectViewSet.as_view({
    'get':'list',
    'post':'create'
})

project_detail = ProjectViewSet.as_view({
    'get' :'retrieve',
    'put' :'update',
    'patch':'partial_update'
})

contributor_list_create = ContributorViewSet.as_view({
    'get':'list',
    'post':'create'
})

contributor_delete = ContributorViewSet.as_view({
    'delete':'destroy'
})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup/', RegisterView.as_view(), name='signup'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/projects/', project_list_create, name='project'),
    path('api/projects/<int:pk>/', project_detail, name='project-detail'),
    path('api/projects/<int:project_id>/contributors/',contributor_list_create,name='contributors-list-create'),
    path("api/projects/<int:project_id>/contributors/<int:pk>/", contributor_delete, name="contributors-delete"),
    path('api/projects/<int:project_id>/issues/', issue_list_create, name='project-issues'),
    path('api/projects/<int:project_id>/issues/<int:pk>/', issue_detail, name='issue-detail'),
    path('api/projects/<int:project_id>/issues/<int:issue_id>/comments/',comment_list_create,name='comment-list-create'),
    path('api/projects/<int:project_id>/issues/<int:issue_id>/comments/<int:pk>/',comment_detail,name='comment-detail'),
]   

