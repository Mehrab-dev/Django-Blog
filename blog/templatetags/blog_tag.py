from django import template
from blog.models import Post , Category

register = template.Library()

@register.inclusion_tag('popularposts.html')
def popular() :
    posts = Post.objects.filter(status=1).order_by('published_date')[:3]
    return {'posts':posts}

@register.inclusion_tag('category.html')
def category() :
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories :
         cat_dict[name]=posts.filter(category=name).count()
    return {'categories' : cat_dict}