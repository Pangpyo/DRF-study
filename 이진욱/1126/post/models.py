from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.CharField(max_length=80)
    email = models.CharField(max_length=80)


class Comment(models.Model):
    content = models.CharField(max_length=80)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE,  related_name='recomment', null=True)
    article = models.ForeignKey(Post, on_delete=models.CASCADE)
