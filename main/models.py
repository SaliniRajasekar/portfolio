from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project/')
    github_link = models.URLField(blank=True)

    def __dtr__(self):
        return self.title
