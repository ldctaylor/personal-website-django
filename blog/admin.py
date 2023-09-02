from django.contrib import admin
from blog.models import Post, Category, Comment

# class AuthorAdmin(admin.ModelAdmin):
#     

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'slug', 'created_on', 'last_modified', 'featured')
    prepopulated_fields={'slug': ('title',)}
    list_filter = ('status',)

class CategoryAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    list_display = ('truncate_comment','name', 'email','created_on', 'post', 'status')
    list_filter = ('status', 'created_on')
    search_fields = ('name', 'email', 'content')

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
