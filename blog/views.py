from django.shortcuts import render , get_object_or_404
from .models import Post

def blog(request) :
    posts = Post.objects.filter(status=1)
    context = {'posts' : posts}
    return render(request,'blog-home.html',context)

def blog_single(request,pk) :
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts,pk=pk)

    context = {'posts' : posts}
    return render(request,'blog-single.html',context)