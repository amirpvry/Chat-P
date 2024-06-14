from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length= 256)
    email = models.EmailField()
    subject = models.CharField(max_length= 255)
    

    message =models.TextField()
    count_views = models.IntegerField(default=0)
    # status =models.BooleanField(default=False)
    # publish_date= models.DateTimeField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    

    
    

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return "{} - {}".format(self.name, self.id)