from django.shortcuts import render
from .models import Post
from .forms import NewsletterForm
from django.urls import reverse
from django.http import HttpResponseRedirect

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


def newsletter(request) :
    if request.method == 'POST' :
        form = NewsletterForm(request.POST) 
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect(reverse('blog:blog_home'))
    form = NewsletterForm()
    context = {'form':form}
    return render (request,'blog/blog-home.html',context)