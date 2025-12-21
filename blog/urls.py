from django.urls import path
from . import views


# create path

app_name = 'blog'


urlpatterns = [
    path('blog/',views.blog_home,name='blog_home'),
    path('blog/<int:pk>/',views.blog_single,name='blog_single'),
    path('search/',views.blog_search,name='search'),
    path('category/<str:cat_name>/',views.blog_category,name='category'),
    path('newsletter/',views.newsletter,name='newsletter'),
    path('blog/tag/<str:tag_name>/',views.blog_tag,name='tag')

]