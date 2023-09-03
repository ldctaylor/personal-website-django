from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=False)
    excerpt = HTMLField(null=True)
    status = models.CharField(max_length=10, choices=options, default='draft')
    content = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories=models.ManyToManyField('Category', related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    objects = models.Manager() #default manager
    newmanager = NewManager() #custom manager

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail_post", kwargs={"slug": self.slug})
    
    class Meta:
        ordering = ('-created_on',)

class Comment(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    status = models.BooleanField(default=True) #can be used for moderating / disabling comments without deleting

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return self.content[slice(50)]
    
    def truncate_comment(self): # for use in admin screen
        return self.content[:25]
