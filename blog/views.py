from django.shortcuts import render
from .models import Post


# create functions
def blog_home(request) :
    posts = Post.objects.filter(status=True)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_search(request) :
    posts = Post.objects.filter(status=True)
    if request.method == 'GET' :
        posts = posts.filter(content__contains = request.GET.get('search'))
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_category(request,cat_name) :
    posts = Post.objects.filter(status=True)
    posts = posts.filter(category__name__iexact = cat_name)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)
