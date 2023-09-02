from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from blog.models import Post, Comment 
from .forms import CommentForm
from django.views.generic import ListView, DetailView

class Index(ListView):
    model = Post
    queryset = Post.newmanager.all().order_by('-created_on')
    template_name = 'blog/index.html'
    paginate_by = 5

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
        form = CommentForm()

        return context

class LikePost(View):
    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        if post.likes.filter(pk=self.request.user.id).exists():
            post.likes.remove(request.user.id)
        else:
            post.likes.add(request.user.id)
        post.save()
        return redirect('detail_post', slug=post.slug)

# def blog_category(request, category):
#     posts = Post.objects.filter(
#         categories__name__contains=category
#     ).order_by(
#         '-created_on'
#     )
#     context = {
#         'category': category,
#         'posts': posts
#     }

#     return render(request, 'blog_category.html', context)

# def blog_detail(request, pk):
#     post = Post.objects.get(pk=pk)

#     form = CommentForm()
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = Comment(
#                 author=form.cleaned_data['author'],
#                 body=form.cleaned_data['body'],
#                 post=post
#             )
#             comment.save()

#     comments = Comment.objects.filter(post=post)
#     context = {
#         'post': post,
#         'comments': comments,
#         'form': form,
#     }

#     return render(request, 'blog_detail.html', context)
