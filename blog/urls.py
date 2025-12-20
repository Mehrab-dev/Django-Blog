from django.urls import path
from . import views


# create path

app_name = 'blog'


urlpatterns = [
    path('blog/',views.blog_home,name='blog_home'),
    path('search/',views.blog_search,name='search'),
    path('category/<str:cat_name>/',views.blog_category,name='category')

]