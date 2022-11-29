from django.urls import path, include
from .views import ArticlesViewset
from rest_framework.routers import DefaultRouter


# 아티클 목록보여주기
article_list = ArticlesViewset.as_view(
    {
        "get": "list",
        "post": "create",
    }
)


# 아티클 디테일 보여주기 + 수정 +삭제

article_detail = ArticlesViewset.as_view(
    {"get": "retrieve", "put": "update", "delete": "destroy"}
)

urlpatterns = [
    path("Articles/", article_list),
    path("Articles/<int:pk>/", article_detail),
]


router = DefaultRouter()

router.register("Articles", ArticlesViewset)

urlpatterns = [path("", include(router.urls))]
