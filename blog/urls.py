from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
path('blog/',views.blog,name='blog_home'),
path('blog/<int:pk>',views.blog_single,name='blog_single'),

]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)