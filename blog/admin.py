from django.contrib import admin
from .models import Post , Category

class PostAdmin(admin.ModelAdmin) :
    list_display = ['title','author','status','created_date','published_date']
    list_filter = ['status','author']
    search_fields = ['status','author']

admin.site.register(Category)
admin.site.register(Post,PostAdmin)