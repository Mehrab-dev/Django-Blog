from django.shortcuts import render


# create functions
def blog_home(request) :
    return render(request,'blog/blog-home.html')
