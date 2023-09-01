from django.contrib import admin
from projects.models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')

admin.site.register(Project, ProjectAdmin)