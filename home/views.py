from django.shortcuts import render
from home.forms import NewsletterForm
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
        form = NewsletterForm(request.POST)
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect(reverse('home:home_page'))
    else :
        form = NewsletterForm()
    context = {'form':form}
    return render(request,'base.html',context)
            