# blog/urls.py

from django.urls import path
from . import views
from .views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
    # path("<int:pk>/", views.blog_detail, name='blog_detail'),
    # path('<category>/', views.blog_category, name='blog_category'),
]