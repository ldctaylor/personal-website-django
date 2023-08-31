from django.contrib import admin
from blog.models import Post, Category, Comment

# class AuthorAdmin(admin.ModelAdmin):
#     

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'slug', 'created_on', 'last_modified', 'featured')

class CategoryAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
