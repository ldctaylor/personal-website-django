# portfolio/urls.py

from django.contrib import admin
from django.urls import path, include
from blog.views import Featured
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static

from .sitemaps import PostSitemap, ProjectSitemap

sitemaps = {
    'posts': PostSitemap,
    'projects': ProjectSitemap,
}

urlpatterns = [
    path('', Featured.as_view(), name='featured'),
    path('opsroom/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('blog/', include('blog.urls')),
    path('accounts/', include('users.urls')),
    path("sitemap.xml", sitemap, {'sitemaps': sitemaps},),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
