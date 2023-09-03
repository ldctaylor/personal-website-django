# blog/urls.py

from django.urls import path, include
from . import views
from .views import Index, DetailPostView, LikePost, Featured

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', Index.as_view(), name='index'),
    path('featured/', Featured.as_view(), name='featured'),
    path('category/<category>/', views.blog_category, name='category'),
    path("<slug:slug>/", DetailPostView.as_view(), name='detail_post'),
    path("<slug:slug>/like/", LikePost.as_view(), name='like_post'),
]