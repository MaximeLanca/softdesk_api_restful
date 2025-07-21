from django.db import models
from django.conf import settings
from projects.models import Project

class Issue(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    status = models.CharField(max_length=128)
    tag = models.CharField(max_length=128)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name="issues")
    assignee = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="issue")

    def __str__(self):
        return self.title

