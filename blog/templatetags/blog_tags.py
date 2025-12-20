from django import template
from blog.models import Post , Category

register = template.Library()

@register.inclusion_tag('blog/blog-popularpost.html')
def popularpost() :
    posts = Post.objects.filter(status=True).order_by('-created_date')[:3]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-category.html')
def category() :
    posts = Post.objects.filter(status=True)
    categories = Category.objects.all() 
    cat_dict = {}
    for name in categories :
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories':cat_dict}
