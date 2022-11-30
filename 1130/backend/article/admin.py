from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_filter = ("title", "description")
    list_display = ("title", "description")
