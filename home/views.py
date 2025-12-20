from django.shortcuts import render
from home.forms import ContactForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# create function
def home_page(request) :
    return render(request,'index.html')

def about_page(request) :
    return render(request,'about.html')


def contact(request) :
    if request.method =='POST' :
        form = ContactForm(request.POST)
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect(reverse('home:contact_page'))
    form = ContactForm()
    context = {'form':form}
    return render(request,'contact.html',context)
