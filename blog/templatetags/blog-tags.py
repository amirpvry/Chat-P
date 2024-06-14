from django import template
from blog.models import post
from blog.models import categories

register = template.Library()

@register.simple_tag(name= 'totalpost')
def hello():
    return post.objects.filter(status=True).count()

@register.simple_tag(name= 'blogpost')
def hello():
    return post.objects.filter(status=True)

@register.filter(status=True)
def char_short(value):
    if len(value) > 20:
        return value[:20] + '...'
    else:
        return value
@register.inclusion_tag("pop.html")
def popular(a=3):
    posts=post.objects.filter(status=True).order_by('-publish_date')[:a]
    return {'posts': posts}
@register.inclusion_tag("blog/blog-category.html")
def categoryblog():
    catdict = {}
    posts=post.objects.filter(status=True)
    categorys=categories.objects.all()
    catdict = {}
    for name in categorys:
     catdict[name]=posts.filter(categories=name).count()
    return {'categorys': catdict}
@register.inclusion_tag("blog/blog-search.html")
def search():
    posts=post.objects.filter(status=True)
    return {'posts': posts}
