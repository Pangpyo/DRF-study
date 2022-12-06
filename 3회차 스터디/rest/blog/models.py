from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='reply', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.CharField(max_length=100)
    created_at = models.DateTimeField('생성시간', auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)