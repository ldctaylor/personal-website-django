from django.contrib.sitemaps import Sitemap
from blog.models import Post
from projects.models import Project

class PostSitemap(Sitemap):
    def items(self):
        return Post.newmanager.all()
    
    def lastmod(self, obj):
        return obj.last_modified
    
class ProjectSitemap(Sitemap):
    def items(self):
        return Project.objects.all()
