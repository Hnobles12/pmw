from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    todos = models.JSONField()
    