from django.db import models
from django import settings

class Project(models.Model):
    title = models.CharField(max_length=128)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,related_name="owned_projects")
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="contributions")
    project = models.ForeignKey(to=Project,on_delete=models.CASCADE,related_name="contributors")
    
    class Meta:
        unique_together = ('user', 'project')

    def __str__(self):
        return f"{self.user.username} → {self.project.title}"