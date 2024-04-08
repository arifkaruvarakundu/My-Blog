from django.urls import path

from blog.views import *

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('category/<str:category>/', BlogCategoryView.as_view(), name='blog-category'),
    path('tag/<str:tag>/', BlogTagView.as_view(), name='blog-tag'),
    path('author/<str:author_username>/', BlogAuthorView.as_view(), name='blog-author'),

    # Add other URLs as needed
]