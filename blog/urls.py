# blog/urls.py

from django.urls import path, include
from . import views
from .views import Index, DetailPostView, LikePost, Featured

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', Index.as_view(), name='index'),
    path('<str:slug>/', DetailPostView.as_view(), name='detail_post'),
    path("<int:pk>/", DetailPostView.as_view(), name='detail_post'),
    path("<int:pk>/like/", LikePost.as_view(), name='like_post'),
    path('featured/', Featured.as_view(), name='featured'),
    # path('<category>/', views.blog_category, name='blog_category'),
]