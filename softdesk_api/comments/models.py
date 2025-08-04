from django.db import models
from issues.models import Issue
from django.conf import settings
import uuid
from django.utils import timezone

class Comment(models.Model):
    description = models.TextField()
    issue = models.ForeignKey(Issue,on_delete=models.CASCADE,related_name="comments")
    assignee = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="comments",null=True, blank=True)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="owned_comments",null=True,blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

