from django.urls import path, include
from rest_framework import routers
from . import views

app_name = "articles"
router = routers.DefaultRouter()
router.register("articles", views.ArticleViewSet, basename="article")
router.register("comment", views.CommentViewSet, basename="comment")


urlpatterns = [path("", include(router.urls))]
