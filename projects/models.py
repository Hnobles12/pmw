from django.db import models
import json

# Create your models here.
class Todo(models.Model):
    pass

class Project(models.Model):
    title = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    # todos = models.JSONField()
    description = models.TextField(default="")
    notes = models.TextField(default="")

    def as_json(self):
        print(str(self.title))
        return json.dumps({"title": str(self.title)})

    def as_dict(self):
        return {
            'id': self.id,
            'title': str(self.title),
            'owner': str(self.owner),
            'created':str(self.created),
            'modified':str(self.modified)
        }
