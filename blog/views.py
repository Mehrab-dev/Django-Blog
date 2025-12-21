from django.shortcuts import render , get_object_or_404
from .models import Post
from .forms import NewsletterForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from taggit.models import Tag

# create functions
def blog_home(request) :
    posts = Post.objects.filter(status=True)
    tags = Tag.objects.all()
    context = {'posts':posts,'tags':tags}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pk) :
    posts = Post.objects.filter(status=True)
    post = get_object_or_404(posts,pk=pk)
    context = {'post':post}
    return render(request,'blog/blog-single.html',context)

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

def blog_tag(request,tag_name) :
    tag = get_object_or_404(Tag,name__iexact = tag_name)
    posts = Post.objects.filter(status=True,tags__name__iexact=tag.name)
    tags = Tag.objects.all()
    context = {'posts':posts,'tags':tags}
    return render(request,'blog/blog-home.html',context)



def newsletter(request) :
    if request.method == 'POST' :
        form = NewsletterForm(request.POST) 
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect(reverse('blog:blog_home'))
    form = NewsletterForm()
    context = {'form':form}
    return render (request,'blog/blog-home.html',context)