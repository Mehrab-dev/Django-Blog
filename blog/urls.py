from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
path('blog/',views.blog,name='blog_home'),
path('blog/single/',views.blog_single,name='blog_single')

]