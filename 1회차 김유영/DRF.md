1. Using **HTTP protocol**
2. **Convenient** resource management
3. Platform **independent** 



## 원칙

1. Uniform Interface
   - 데이터를 식별 가능하게 해야한다
   - 구체적으로 URL만 보고도 **어느 데이터**를 **어떤 상태**로 전송해야 하는지 구별할 수 있어야 함

2. Client Server
   - **클라이언트와 서버는 반드시 분리**되어야 하며, **클라이언트는 데이터를 서버에 요청**하고 **서버는 클라이언트의 요청에 따른 데이터를 응답**해야 함

3. Stateless
   - HTTP 프로토콜을 따르기 때문에 HTTP 특징과 같이 상태를 저장하지 않으며, 요청에 모든 정보가 담겨 한 번에 전송해야 함

4. Cacheable
   - 요청을 통해 보내는 자료들은 저장되어야 함
   - 이를 통해서 저장된 자료들을 주고 받을 때 속도를 향상시킬 수 있음

5. Layered System
   - 요청된 정보를 검색하는데 계층 구조로 분리되어 있어야 함
   - 중간 서버 등을 둬 서버 확장성을 보장함

6. Code on Demand
   - 보통 서버는 XML이나 JSON으로 응답하지만, 필요한 경우 코드 자체를 데이터로 클라이언트에 전달할 수 있다.

## URL 네이밍 규칙

#### 1.  명사를 사용한다.

나쁜 예

www.fomagran.com/get-users

좋은 예

www.fomagran.com/users



#### 2. 소문자를 사용한다.

나쁜 예

www.fomagran.com/Users

좋은 예

www.fomagran.com/users



#### 3. 복수형을 사용한다.

나쁜 예

www.fomagran.com/user

좋은 예

www.fomagran.com/users



#### 4. 구분자는 "-"(하이픈)을 사용한다. (카멜 케이스도 허용되지 않음)

나쁜 예

[www.fomagran.com/](http://www.fomagran.com/)very_good_users

[www.fomagran.com/](http://www.fomagran.com/)veryGoodUsers

좋은 예

[www.fomagran.com/](http://www.fomagran.com/)very-good-users



#### 5. url의 마지막엔 슬래쉬를 포함하지 않음

나쁜 예

[www.fomagran.com/](http://www.fomagran.com/)very-good-users/

좋은 예

[www.fomagran.com/](http://www.fomagran.com/)very-good-users

#### 6. 파일 확장자는 포함하지 않음


나쁜 예

[www.fomagran.com/](http://www.fomagran.com/)photos/image.jpg

좋은 예

[www.fomagran.com/](http://www.fomagran.com/)photos/image



# 상속받는 클래스의 추상화(패턴화)

#### APIView

```python
from .models import Blog
from .serializer import BlogSerializer

# Create your views here.

# APIView를 사용하기 위해 import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Blog의 목록을 보여주는 역할
# 1. 전체 목록 보여주기(GET) 2. 새로운 Blog 객체 등록하기(POST)
class BlogList(APIView):
    # Blog list를 보여줄 때
    def get(self, request):
        blogs = Blog.objects.all()
        # 여러 개의 객체를 serialzation하기 위해 many=True로 설정
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    # 새로운 Blog 글을 작성할 때
    def post(self, requset):
        # request.data는 사용자의 입력 데이터
        serializer = BlogSerializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data)


# Blog의 detail을 보여주는 역할
# 1. Blog 객체의 detail 보여주기(GET) 2. Blog 객체 수정하기(PUT) 3. Blog 객체 삭제하기(DELETE)
class BlogDetail(APIView):
    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404

    # Blog의 detail 보기
    def get(self, request, pk, format=None):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    # Blog 수정하기
    def put(self, request, pk, format=None):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Blog 삭제하기
    def delete(self, request, pk, format=None):
        blog = self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```



#### Mixins

```python
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import generics
from rest_framework import mixins

# Blog의 목록을 보여주는 역할
class BlogList(mixins.ListModelMixin, 
                  mixins.CreateModelMixin, 
                  generics.GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class =BlogSerializer

	# Blog list를 보여줄 때
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
	
	# 새로운 Blog 글을 작성할 때
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# Blog의 detail을 보여주는 역할
class BlogDetail(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

	# Blog의 detail 보기
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

	# Blog 수정하기
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

	# Blog 삭제하기
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
```

- CBC 상속 때문에 간결해짐

- BlogList와 BlogDetail라는 클래스를 살펴보면 인자로 mixing.ListModelMixin,mixins,CreateModelMixin등을 받음

  그것으로 views.py 상단에 import해준 mixins에서 상속 받음



#### Generic CBV

```python
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import generics

# Blog의 목록을 보여주는 역할
class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# Blog의 detail을 보여주는 역할
class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
```

- Generic CBV에서 상속받은 **generics.py** 코드를 확인해보면 

  각각의 HTTP method 기능을 하는 클래스가 구현되어 있음

  예를 들어 CreateAPIView는 새로운 객체를 생성하는 POST의 기능을,

  ListAPIView는 객체의 전체 목록을 보여주는 GET의 기능을 수행

- **Blog 객체의 전체 목록 보기 + 새로운 객체 등록**을 위해 **ListCreateAPIView** 클래스와

  **Blog detail 보기 + 객체 수정 + 객체 삭제**를 위해 **RetrieveUpdateDestroyAPIView** 클래스를 상속



#### ViewSets 

```python
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import viewsets

# Blog의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
```

- 코드가 이렇게 간결할 수 있었던 것은 클래스의 **상속** 개념을 활용



##### ViewSets urls.py

```python
* as_view() 활용

from django.urls import path
from .views import BlogViewSet

# Blog 목록 보여주기
blog_list = BlogViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

# Blog detail 보여주기 + 수정 + 삭제
blog_detail = BlogViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns =[
    path('blog/', blog_list),
    path('blog/<int:pk>/', blog_detail),
]
```

- as_view() 함수를 사용하여 mapping 관계를 처리 
- 함수를 인자로는 http method와 처리할 함수의 이름을 작성
- 처리할 함수의 이름 list, create, retrieve, update, destory등이 있으며 이것은 viewsets.py에서 확인



```python
* router 활용

from django.urls import path, include
from .views import BlogViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# 첫 번째 인자는 url의 prefix
# 두 번째 인자는 ViewSet
router.register('blog', BlogViewSet)

urlpatterns =[
    path('', include(router.urls))
]
```

- 다음으로는 rest framework의 DefaultRouter라는 객체를 생성하여,

  mapping 하고자 하는 view를 등록