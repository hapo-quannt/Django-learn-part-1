# posts/urls.py

from django.urls import path, re_path
from django.contrib import admin
from posts.views import (
  ListPostView,
CreatePostView,
UpdatePostView
)

urlpatterns = [
    re_path(r'^list-posts/$', ListPostView.as_view(), name='list-posts'),
    re_path(r'^create-post/$', CreatePostView.as_view(), name='create-post'),
    re_path(r'^update-post/(?P<pk>[-\w]+)$', UpdatePostView.as_view(), name='update-post'),
]
