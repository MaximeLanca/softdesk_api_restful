from django.db import models
from issues.models import Issue
from django.conf import settings

class Comment(models.Model):
    description = models.TextField()
    issue = models.ForeignKey(Issue,on_delete=models.CASCADE,related_name="comments")
    assignee = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="comments",null=True, blank=True)

    def __str__(self):
        return self.title

