# Django Rest  Framework

## 💡REST API란?

> REST : Representational State Transfer
API : Application Programming Interface
> 
- REST API를 통해 REST 서버는 API를 제공, 클라이언트는 사용자 인증이나 컨텐스트(세션, 로그인정보)등을 직접 관리하는 구조로 각각의 역할이 확실히 구분되기 때문에 클라이언트와 서버에서 개발해야 할 내용이 명확해지고 서로간 의존성이 줄어들게 된다.
- 데이터베이스 내부의 자료를 직접 전송하는 것이 아니라 HTML, XML, JSON와 같은 데이터 형태를 통해 제공하게 되고, 사용자들이 접근할 수 있게 되는 것 재사용성 증대

> 👍프론트앤드 개발자와의 협업을 위한 것
👍 급격하게 높아지는 코드의 재활용성 -> 생산성 상승
> 
- 한개의 API가 프론트엔드에서 여러개의 페이지에 이용된다.
- views.py에서 하나의 템플릿에 하나의 클래스,함수가 호출되던 것과는 다르다.

**METHOD역할**

## POST

POST를 통해 해당 URI를 요청하면 리소스를 생성합니다.

## GET

GET를 통해 해당 리소스를 조회합니다. 리소스를 조회하고 해당 도큐먼트에 대한 자세한 정보를 가져온다.

## PUT

PUT를 통해 해당 리소스를 수정합니다.

## DELETE

DELETE를 통해 리소스를 삭제합니다.

### serializer

1. 모델생성

```
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.Serializer):
id = serializers.IntegerField(read_only=True)
title = serializers.CharField(required=False, allow_blank=True, max_length=100)
code = serializers.CharField(style={'base_template': 'textarea.html'})
linenos = serializers.BooleanField(required=False)
language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
```

```
def create(self, validated_data):
    """
    Create and return a new `Snippet` instance, given the validated data.
    """
    return Snippet.objects.create(**validated_data)

def update(self, instance, validated_data):
    """
    Update and return an existing `Snippet` instance, given the validated data.
    """
    instance.title = validated_data.get('title', instance.title)
    instance.code = validated_data.get('code', instance.code)
    instance.linenos = validated_data.get('linenos', instance.linenos)
    instance.language = validated_data.get('language', instance.language)
    instance.style = validated_data.get('style', instance.style)
    instance.save()
    return instance

```

```

```

1. serializer 직렬화

```
모델 데이터 생성 (power shell)

snippet = Snippet(code='foo = "bar"\\n')
snippet.save()

snippet = Snippet(code='print("hello, world")\\n')
snippet.save()

```

```

직렬화 데이터로 생성 (마지막 지정 데이터 기준으로 직렬화 )

serializer = SnippetSerializer(snippet)
serializer.data

```

```
저장된 데이터 확인 (딕셔너리로 묶인 값들 확인 가능 )
serializer.data
# {'id': 2, 'title': '', 'code': 'print("hello, world")\\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}

ordereddict상태 아직 json으로 만들 수 없음

```

```
json render 시키기  (시리얼라이즈 후에는 제이슨렌더러를 통해 제이슨 파일로 변환시킬 수 있다. )
```content = JSONRenderer().render(serializer.data)
content
# b'{"id": 2, "title": "", "code": "print(\\\\"hello, world\\\\")\\\\n", "linenos": false, "language": "python", "style": "friendly"}'
이때 타입을 확인해보면 content의 type은 byte인걸 확인 가능하다. (제이슨렌더를 통해 문자열로 변경)

```

1. Deserializer 역직렬화

```
기존의 있던 data(byte타입)데이터를 딕셔너리로 만들어준다.

import io

stream = io.BytesIO(content)
data = JSONParser().parse(stream)

```

```
딕셔너리를 형태의 데이터를 유효성검사를 해준 후 오브젝트의 형태로 데이터베이스에 저장
serializer = SnippetSerializer(data=data) # 디시리얼라이즈 과정에서는 data에 넣겠다 명시해야한다.
serializer.is_valid()
# True
serializer.validated_data
# OrderedDict([('title', ''), ('code', 'print("hello, world")\\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
serializer.save()
# <Snippet: Snippet object>

```

# view , viewSet

APIView, MIxins, Generic CBV 랑 Viewsets (최종진화)

기존의 펑션베이스뷰는 GET이냐 POST에 따라서 어떤 리스폰스를 내보낼지 결정을 했음

대상에 따라서 함수를 구분지어줘야했다.  VIEW마다 URL 엔드포인트 지정

DRF에서는 클래스베이스뷰를 사용.

장점 - 모델이랑 시리얼라이즈만 한다면,  GET이랑 POST요청을 알아서 해줌,

리스트뷰와 디테일뷰는 구분되어져있음, 펑션베이스뷰에서와 마찬가지로 엔드포인트를 각각 다르게 지정해줘야 한다. 

viewSET = 클래스뷰의 최종진화 유저리스트와 유저디테일을 묶어버림, 

 어떻게 구분짓느냐 ?  URL에서 받을때 어떤 액션을 취할지 URL에서 명시해준다.

user_list OR user_detail

# Router

```
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet,basename="snippet")
router.register(r'users', views.UserViewSet,basename="user")
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

router.register(r'snippets', views.SnippetViewSet,basename="snippet")

r은 type str을 표현 할 때 백슬래쉬를 처리해주기 위해 사용한다
```

`ViewSet`클래스는  `View`실제로 URL conf를 직접 작성할 필요가 없다,  . 리소스를 뷰와 URL에 연결하는 규칙은 `Router`클래스를 사용하여 자동으로 처리할 수 있음 

 우리가 해야 할 일은 적절한 `ViewSet`를 라우터에 등록하고 나머지는 라우터가 처리하도록 하는 것입니다. 

reuqest에 따라 url을 결정해줌