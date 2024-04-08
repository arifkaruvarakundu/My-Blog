from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from blog.models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Your template for listing blogs
    context_object_name = 'blogs'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comment_set.filter(parent=None)  # Fetch top-level comments
        return context
    
class BlogCategoryView(ListView):
    model = Post
    template_name = 'blog_list.html'  # Same template as blog list
    context_object_name = 'blogs'

    def get_queryset(self):
        category = self.kwargs['category']
        return Post.objects.filter(categories__name=category)

class BlogTagView(ListView):
    model = Post
    template_name = 'blog_list.html'  # Same template as blog list
    context_object_name = 'blogs'

    def get_queryset(self):
        tag = self.kwargs['tag']
        return Post.objects.filter(tags__name=tag)
    
class BlogTagView(ListView):
    model = Post
    template_name = 'blog_list.html'  # Same template as blog list
    context_object_name = 'blogs'

    def get_queryset(self):
        tag = self.kwargs['tag']
        return Post.objects.filter(tags__name=tag)

class BlogAuthorView(ListView):
    model = Post
    template_name = 'blog_list.html'  # Same template as blog list
    context_object_name = 'blogs'

    def get_queryset(self):
        author_username = self.kwargs['author_username']
        return Post.objects.filter(author__username=author_username)

    