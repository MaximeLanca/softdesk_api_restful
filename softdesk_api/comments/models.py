from django.db import models
from issues.models import Issue
from django import settings

class Comment(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    issue = models.ForeignKey(Issue,on_delete=models.CASCADE,related_name="issues")
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="issue")

    def __str__(self):
        return self.title

