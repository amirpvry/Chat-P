from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class categories(models.Model):
    name= models.CharField(max_length=256)
    def __str__(self) :
        return self.name
    
class post(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length= 256)

    content =models.TextField()
    categories = models.ManyToManyField(categories)
    count_views = models.IntegerField(default=0)
    status =models.BooleanField(default=False)
    image = models.ImageField(upload_to='blog/' , default='default.jpg')
    tags = TaggableManager()
    publish_date= models.DateTimeField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    login_require = models.BooleanField(default=False)

    

    class Meta:
        ordering = ['-create_date']
        # verbose_name = "amirpost"
        # verbose_name_plural = "amirpost"

        


    def __str__(self):
        return "{} - {}".format(self.title, self.id)
    
    def stippers(self):
        return self.content[:100] + '...'
    
    def get_absolute_url(self):
        return reverse('blog:blog-home', kwargs= {"pid": self.id})
    
class comment(models.Model):
    post = models.ForeignKey(post,on_delete=models.CASCADE)
    name= models.CharField(max_length=256)
    email = models.EmailField()
    subject = models.CharField(max_length= 255)
    message =models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    

    class Meta:
        ordering = ['-create_date']
        # verbose_name = "amirpost"
        # verbose_name_plural = "amirpost"


# Create your models here.
