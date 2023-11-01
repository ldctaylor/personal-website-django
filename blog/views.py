from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from blog.models import Post, Comment, Category 
from .forms import CommentForm
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator 

class Index(ListView):
    model = Post
    queryset = Post.newmanager.all().order_by('-created_on')
    template_name = 'blog/index.html'
    paginate_by = 6

class Featured(ListView):
    model = Post
    queryset = Post.newmanager.filter(featured=True).order_by('-created_on')
    template_name = 'blog/featured.html'
    paginate_by = 3

class DetailPostView(DetailView):
    model = Post 
    template_name = 'blog/blog_post.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailPostView, self).get_context_data(*args, **kwargs)
        context['liked_by_user'] = False
        post = get_object_or_404(Post, slug=self.kwargs.get('slug'), status='published') # ensures only published posts are retrieved
        comments = post.comments.filter(status=True)
        context['comments'] = comments
        if post.likes.filter(pk=self.request.user.id).exists():
            context['liked_by_user'] = True
        if self.request.user.is_authenticated:
            context['comment_form'] = CommentForm(instance=self.request.user)

        return context
    
    def post(self, request, *args, **kwargs):
        new_comment = Comment(content=request.POST.get('content'),name=self.request.user,post=self.get_object())  
        new_comment.save()
        return HttpResponseRedirect(f'/blog/{self.get_object().slug}/')

class LikePost(View):
    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        if post.likes.filter(pk=self.request.user.id).exists():
            post.likes.remove(request.user.id)
        else:
            post.likes.add(request.user.id)
        post.save()
        return redirect('detail_post', slug=post.slug)

def blog_category(request, category):
    posts = Post.newmanager.filter(
        categories__name__contains=category, status='published'
    ).order_by(
        '-created_on'
    )
    paginated = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginated.get_page(page_number)

    context = {
        'category': category,
        'page_obj': page_obj

    }

    return render(request, 'blog/category.html', context)

def category_list(request):
    category_list = Category.objects.all()
    context = {
        'category_list': category_list,
    }

    return context