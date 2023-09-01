from django.db import models
from django.urls import reverse

class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, null=False)
    description = models.TextField()
    technology = models.CharField(max_length=25)
    image = models.FilePathField(path="/img")

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug})
