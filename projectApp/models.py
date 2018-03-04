from django.db import models
from Accounts.models import Staff


# Create your models here.
class project(models.Model):
    name = models.CharField(max_length=200)
    started_on = models.DateTimeField(auto_now_add=False, auto_now=True)
    ended_on = models.DateTimeField(auto_now_add=False, auto_now=False)
    description = models.TextField()

    def __str__(self):
        return self.name


class part(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(project, on_delete=models.CASCADE)
    worker = models.ForeignKey(Staff, on_delete=models.CASCADE)
    files = models.FileField()
    direction = models.TextField()

    def __str__(self):
        return self.name


class completed_task(models.Model):
    project = models.ForeignKey(project, on_delete=models.CASCADE)
    part = models.ForeignKey(part, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    files = models.FileField()
    recommendation = models.TextField()

    def __str__(self):
        return self.project.name
