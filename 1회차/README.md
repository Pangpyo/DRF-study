# DRF STUDY 1회차

## REST?

* REST : Representational State Transfer
  * HTTP protocol을 사용한다
  * 자원 관리가 편리하다
  * 플랫폼에 종속되지 않는다
  * ![image-20221125010150861](C:\Users\asus\AppData\Roaming\Typora\typora-user-images\image-20221125010150861.png)
  * 이전과 같이 url로 기능을 분리하는것이 아닌, url을 고정시키고 HTTP 메서드를 통해 자원 관리를 한다.
  * HTTP 메서드를 사용하는 모든 플랫폼에서 사용 가능하다.
* 기존 장고와의 차이?
  * ![image-20221125010601533](C:\Users\asus\AppData\Roaming\Typora\typora-user-images\image-20221125010601533.png)
  * 기존 장고는 view와 template이 강하게 결합되어있다.
  * 웹만 만든다면 괜찮다. 하지만 모바일 어플리케이션에 대응하지 못한다.
  * 이에 대응하기위해 REST를 사용한다.

## Django rest framework 설치

* 장고 설치 후, 

```bash
pip install djangorestframework
pip install markdown 
```

```python
# settings.py

INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

```python
urls.py

urlpatterns = [
    ...
    path('api-auth/', include('rest_framework.urls'))
]
```

## urls.py, views.py 작성해보기

```python
# urls.py

from django.urls import path

from . import views

urlpatterns = [
    path("hello_world/", views.hello_world),
]

# views.py

from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})
```

runserver 한 후 해당 url로 이동하면?

![image-20221125015612310](C:\Users\asus\AppData\Roaming\Typora\typora-user-images\image-20221125015612310.png)

이러한 화면이 뜨게된다.