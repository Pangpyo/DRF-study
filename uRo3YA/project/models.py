from django.db import models
from django.conf import settings
from account.models import User



class Blog(models.Model):

    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True,upload_to="image")
    like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="like_post_set" )
    
    def is_like_user(self, user):
        return self.like_user_set.filter(pk=user.pk).exists()
        
    class Meta:
        db_table = 'blog'


class Comment(models.Model):
    blog = models.ForeignKey(Blog, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True, null=False, blank=False)
    comment = models.TextField()

    def __str__(self):
        return self.comment



