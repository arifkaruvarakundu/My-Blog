from django.urls import path
from blog.views import *

urlpatterns = [
    path('blog/<int:pk>/', BlogPostDetailView.as_view(), name='blog-detail'),
    path('category/<str:category>/', BlogCategoryView.as_view(), name='blog-category'),
    path('tag/<str:tag>/', BlogTagView.as_view(), name='blog-tag'),
    path('blog/postComment', PostCommentView.as_view(), name='postComment'),
]