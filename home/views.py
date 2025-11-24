from django.shortcuts import render
from home.models import Newsletter
from django.urls import reverse
from django.http import HttpResponseRedirect


def home(request) :
    return render(request,'index.html')

def about(request) :
    return render(request,'about.html')

def contact(request) :
    return render(request,'contact.html')

def newsletter(request) :
    if request.method == 'POST' :
        form = Newsletter(request.POST)
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect(reverse('home:home_page'))
    form = Newsletter()
    context = {'form':form}
    return render(request,'base.html',context)
            