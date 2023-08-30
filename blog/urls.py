# blog/urls.py

from django.urls import path, include
from . import views
from .views import Index, DetailPostView

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', Index.as_view(), name='index'),
    path("<int:pk>/", DetailPostView.as_view(), name='detail_post'),
    # path('<category>/', views.blog_category, name='blog_category'),
]