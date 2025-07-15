from django.db import models
from django import settings

class Project(models.Model):
    title = models.CharField(max_length = 128)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name = "users")
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

