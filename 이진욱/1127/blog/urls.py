from django.urls import path, include
from .views import BlogViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('blog', BlogViewSet)
router.register('comment', CommentViewSet, basename='comment') # (댓글)

urlpatterns =[
    path('', include(router.urls))
]