from django.db import models
from django.conf import settings

# Create your models here.


class TODO(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField(null=True)
    is_complete = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="todo",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
