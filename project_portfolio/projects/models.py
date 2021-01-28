from django.db import models

class Project(models.Model):
    """
    Project Model
    Defines the attributes of a project
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    technology = models.CharField(max_length=255)
    image = models.FilePathField(path="/img")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_description(self):
        return self.title + ' is a projects: ' + self.description + '.'

    def __repr__(self):
        return self.title + ' is added.'
