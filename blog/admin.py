from django.contrib import admin
from .models import Post , Category , Newsletter , Comment

class PostAdmin(admin.ModelAdmin) :
    list_display = ['title','author','status','created_date','published_date']
    list_filter = ['status','author']
    search_fields = ['status','author']

class CategoryAdmin(admin.ModelAdmin) :
    list_display = ['name','created_date']

class CommentAdmin(admin.ModelAdmin) :
    list_display = ['name','email','subject']
    list_filter = ['email']


admin.site.register(Comment,CommentAdmin)
admin.site.register(Newsletter)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)