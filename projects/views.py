from django.shortcuts import render
from .models import Project

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects' : projects
    }
    return render(request, 'project.html', context)

# def project_detail(request, slug):
#     project = Project.objects.get(slug=slug)
#     context = {
#         'project' : project
#     }
#     return render(request, 'project_detail.html', context)


