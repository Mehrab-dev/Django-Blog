from django.contrib import admin
from .models import Post , Category

class PostAdmin(admin.ModelAdmin) :
    date_hierarchy = 'created_date'
    list_display = ['id','title','author','published_date','counted_view','status']
    list_filter = ['status','author']
    search_fields = ['author']
    list_display_links = ['id','title']


admin.site.register(Post,PostAdmin)
admin.site.register(Category)