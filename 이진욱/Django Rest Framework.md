# Django Rest Framework



DRF는 Django 에서 지원하는 REST API이다.

REST란 REpresentational State Transfer 의 약자로 자원의 이름으로 서버와 클라이언트가 통신하는 방법을 말한다.

웹 뿐만 아니라 모바일 등 다양한 접근 플랫폼에 대응하기 좋다.

HTTP 프로토콜을 사용한다.

<br>

<br>

### pip 설치

```bash
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```

<br>

<br>

### settings.py

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

<br>

<br>

### urls.py

```python
urlpatterns = [
    ...
    path('api-auth/', include('rest_framework.urls'))
]
```

<br>

<br>





# app 폴더



### Models.py

```python
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.CharField(max_length=80)
    email = models.CharField(max_length=80)

```

<br>

<br>

### serializers.py

```python
from rest_framework import serializers
from post.models import Post  # Post 모델 받아오기


# 모델을 기반으로 Serializer 만들기
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post # 모델이 Article 모델이다.
        fields = "__all__" # 모든 필드를 다 다루겠다.
```

<br>

<br>

### views.py

```python
from django.shortcuts import render
from .models import Post
from post.serializers import PostSerializer
from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```



`ModelViewSet` 는 기본적으로 CRUD를 지원한다.



### urls.py

```py
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('post',views.PostViewSet)

urlpatterns = [
    path('',include(router.urls) ),
]
```



`router` 을 사용하면 URL 설정을 다룰 필요가 없다.

