from django.db import models
from django.conf import settings
from projects.models import Project
from django.utils import timezone

class Issue(models.Model):
    ISSUE_PRIORITY = [("LO","Low"),("ME","Medium"),("HI","High")]
    ISSUE_TAG = [("BU","Bug"),("TA","Task"),("FE","Feature")]
    ISSUE_STATUS = [("TD","To do"),("IP","In progress"),("FI","Finished")]
    title = models.CharField(max_length=128)
    description = models.TextField()
    status = models.CharField(max_length=2, choices=ISSUE_STATUS, default="TD")
    priority = models.CharField(max_length=2, choices=ISSUE_PRIORITY, default="LO")
    tag = models.CharField(max_length=2, choices=ISSUE_TAG, default="TA")
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name="issues")
    assignee = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="issue",null=True, blank=True)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="owned_issues",null=True,blank=True)
    created_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

