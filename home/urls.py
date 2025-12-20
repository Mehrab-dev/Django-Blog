from django.urls import path
from . import views

# create path

app_name = 'home'

urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('about/',views.about_page,name='about_page'),
    path('contact/',views.contact,name='contact_page')

]