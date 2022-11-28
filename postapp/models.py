from django.db import models

# Create your models here.

class Post(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    title = models.CharField(max_length=200)
    contents = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)