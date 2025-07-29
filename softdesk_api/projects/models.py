from django.db import models
from django.conf import settings

class Project(models.Model):
    PROJECT_TYPE = [("BE","Back-end"),("FE","Front-end"),("IO","iOS"),("AN","Android")]
    title = models.CharField(max_length=128)
    project_type = models.CharField(max_length=2, choices=PROJECT_TYPE, default="BE")
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="owned_projects")

    def __str__(self):
        return self.title


class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="contributions")
    project = models.ForeignKey(to=Project,on_delete=models.CASCADE,related_name="contributors")
    
    class Meta:
        unique_together = ('user', 'project')

    def __str__(self):
        return f"{self.user.username} → {self.project.title}"