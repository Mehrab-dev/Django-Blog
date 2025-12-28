from django.shortcuts import render , get_object_or_404
from .models import Post , Comment
from .forms import NewsletterForm , CommentForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from taggit.models import Tag
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages

# create functions
@login_required
def blog_home(request) :
    posts = Post.objects.filter(status=True)
    paginator = Paginator(posts,2)
    number_page = request.GET.get('page')
    posts = paginator.get_page(number_page)
    tags = Tag.objects.all()
    context = {'posts':posts,'tags':tags}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pk) :
    posts = Post.objects.filter(status=True)
    post = get_object_or_404(posts,pk=pk)
    if request.method == 'POST' :
        form = CommentForm(request.POST)
        if form.is_valid() :
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request,messages.SUCCESS,'your comment was successfully submit')
        else :
            messages.add_message(request,messages.SUCCESS,'your comment was not registered')
    comments = Comment.objects.filter(approved=True)
    context = {'post':post,'comments':comments}
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