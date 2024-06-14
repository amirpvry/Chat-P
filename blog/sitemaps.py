from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from blog.models import post
from django.urls import reverse


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return post.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.publish_date
    
    def location(self , obj):
        return reverse('blog:blog-home', kwargs= {"pid": obj.id})
