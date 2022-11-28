from django.urls import path, include
from .views import PostViewSet
from rest_framework.routers import DefaultRouter

# 목록 보여주기
post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

# Post detail 보여주기 + 수정 + 삭제
post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

router = DefaultRouter()
# 첫 번째 인자는 url의 prefix
# 두 번째 인자는 ViewSet
router.register('post', PostViewSet)

urlpatterns = [
    path('post/', post_list),
    path('post/<int:pk>/', post_detail),
    path('', include(router.urls))
]