from django.db import models
from django.conf import settings


# Create your models here.


class Articles(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=100)


class Camp(models.Model):
    title = models.CharField(max_length=30)
    local = models.BooleanField(blank=True)
