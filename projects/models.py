from django.db import models
from django.urls import reverse

def user_directory_path(instance, filename):
    return 'projects/{0}/{1}'.format(instance.id, filename)

class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, null=False)
    description = models.TextField()
    technology = models.CharField(max_length=255)
    image = models.ImageField(upload_to=user_directory_path, default='projects/default.svg')
    url = models.URLField(null=True, max_length=255)

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug})