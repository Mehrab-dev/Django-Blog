from django.db import models 
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# create models
class Post(models.Model) :
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    tags = TaggableManager()
    status = models.BooleanField(default=True)
    counted_view = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self) :
        return self.title


class Category(models.Model) :
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.name
    
class Newsletter(models.Model) :
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.email
    