from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from django.views import View
from django.views.generic import ListView, DetailView
from blog.models import *

class BlogListView(ListView):
    model = Post
    template_name = 'blog/blogHome.html'  # Your template for listing blogs
    context_object_name = 'blogs'

    

class BlogCategoryView(ListView):
    model = Post
    template_name = 'home/index.html'  
    context_object_name = 'blogs'

    def get_queryset(self):
        category = self.kwargs['category']
        return Post.objects.filter(categories__name=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class BlogTagView(ListView):
    model = Post
    template_name = 'home/index.html'  
    context_object_name = 'blogs'

    def get_queryset(self):
        tag = self.kwargs['tag']
        return Post.objects.filter(tags__name=tag)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

    


class BlogAuthorView(ListView):
    model = Post
    template_name = 'home/index.html'  # Same template as blog list
    context_object_name = 'blogs'

    def get_queryset(self):
        author_username = self.kwargs['author_username']
        return Post.objects.filter(author__username=author_username)

from django.views import View
from django.shortcuts import redirect
from django.contrib import messages
from .models import Post, Comment

class PostCommentView(View):
    def post(self, request):
        if request.method == 'POST':
            comment_text = request.POST.get('comment')
            user = request.user
            post_id = request.POST.get('postid')
            parent_id = request.POST.get('parentid')
            post = Post.objects.get(id=post_id)

            if parent_id == "":
                # Create a new comment
                comment_obj = Comment(body=comment_text, user=user, post=post)
                comment_obj.save()
                messages.success(request, "Your Comment has been Posted Successfully")
            else:
                # Reply to an existing comment
                parent_comment = Comment.objects.get(id=parent_id)
                comment_obj = Comment(body=comment_text, user=user, post=post, parent=parent_comment)
                comment_obj.save()
                messages.success(request, "Your Reply has been Posted Successfully")

        return redirect('blog-detail', pk=post.id)



from django.db.models import Prefetch

class BlogPostDetailView(DetailView):
    model = Post
    template_name = 'blog/blogPost.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()

        # Increase views count
        # post.views += 1
        post.save()

        # Fetch top-level comments
        comments = Comment.objects.filter(post=post, parent=None).prefetch_related(
            Prefetch('replies', queryset=Comment.objects.filter(parent__isnull=False))
        )

        context['comments'] = comments
        context['user'] = self.request.user

        return context
