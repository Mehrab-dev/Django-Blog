from django import template
from blog.models import Post , Category , Comment

register = template.Library()

@register.simple_tag(name='counted_comment')
def function(pk) :
    return Comment.objects.filter(post=pk,approved=True).count()

@register.filter
def snippets(value,args=10) :
    return value[:args] + '...'


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
