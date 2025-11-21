from django.db import models
from django.contrib.auth.models import User

class Category(models.Model) :
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model) :
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    published_date = models.DateField(null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='blog/',null=True)
    category = models.ManyToManyField(Category)
    status = models.BooleanField(default=True)
    counted_view = models.IntegerField(default=0)
    
    class Meta :
        ordering = ['published_date']

    def __str__(self) :
        return '{} - {}'.format(self.id,self.title)