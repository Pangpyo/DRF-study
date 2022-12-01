## 2022.11.30 DRF study3 - FBV

> FBV 형태는 기존에 배운 django의 views.py에 정의했던 form을 처리하기 위한 function과 유사한 형태를 지니고 있음.

- 그러면 기존에 배운 form을 사용하지 왜 DRF라는 개념을 또다시 도입해서 적용하는걸까?
- https://dlee0129.tistory.com/183
  - 웹페이지는 객체(object)로 구성 되어 있음
  - 객체는 HTML, JPEG 등이 될 수 있음
  - 이 객체는 URL로 지칭함
    - 예를 들어 www.test.com/test/post 라는 주소가 있다고하면 www.test.com은 호스트네임, /test/post가 객체의  path name 이자 object URL임
- 객체로 구성된 웹페이지를 처리하여야 하는데, 이 객체를 처리하는 주체가 VUE, REACT라면? 근데 VUE의 경우 vue.js 파일명에서도 확인가능하듯이 Javascript 기반으로 파생된 애고, 이 vue가 데이터를 처리하기 위해서는  javascript 기반으로 나온 string 기반의 JSON이 자료 형태로 채택될 수 밖에 없었던 것 같음.



> FBV CRUD 작성하기

- 출처: https://velog.io/@jewon119/TIL00.-DRF-FBV%EB%A1%9C-CRUD-%EA%B0%84%EB%8B%A8-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0



```python
# models.py
from django.db import models

class fbv_Post(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField(null=True)
```



```python
# serializers.py
from rest_framework import serializers
from fbvapp.models import fbv_Post

class fbv_PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = fbv_Post
        fields = '__all__'
```



```python
from django.shortcuts import render
from fbvapp.models import fbv_Post
from fbvapp.serializers import fbv_PostSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# GET: 데이터 받음 / POST: 데이터 입력
# api_view가 가장 널리 쓰이는 데코레이터, 이는 FBV에 많이 쓰인다고 공식 레포에서도 말하고 있음.
# 넘어오는 요청 HTTP method가 무엇인지 확인하기 위한 
@api_view(['GET', 'POST'])
def fbv_post_list(request):
    # GET: 글 목록을 조회하거나, 세부 글 내용을 조회하거나.
    if request.method == 'GET':
        # 모든 DB 데이터를 가져와서
        fbv_post = fbv_Post.objects.all()
        # serializer라는 변수에 serializers.py에서 정의했던 class에 fbv_post 데이터를 담고,
		# 이 데이터는 여러 개가 될 수 있어서 many 옵션을 True로 변경
        # 그래서 meta class를 이용한게 아닐까? 클래스 아규먼트로 받은 fbv_post를 커스텀 해야하니까.
        serializer = fbv_PostSerializer(fbv_post, many=True)
        # 그래서 serializer 변수에 담긴 data를 Response를 해주는데
        # 이 Response는 rest_framework의 responses.py에서 가져온거고,
        # 여기서 말하는 Reponse란 정형화된 데이터를 응답해주는 것으로 보임.
        # serializer에서 정형화해줬으니, 일반 HTTPresponse랑은 차이가 있는 것으로 해석됨.
        return Response(serializer.data)
    
    # POST: client가 글 등 Input값이 담긴 데이터를 전송하였을 경우
    elif request.method == 'POST':
        # 사용자 데이터인 request.data를 정의한 fbv_PostSerializer에 아규먼트로 보내서 인스턴스화하고 이를 변수에 담음
        serializer = fbv_PostSerializer(data=request.data)

        # 인스턴스가 유효하다면
        if serializer.is_valid():
            # 인스턴스 저장하고
            serializer.save()
            # 인스턴스 반환해주고, 201 코드를 전달함으로써 성공적으로 요청을 처리하였음을 알림
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 인스턴스가 유효하지 않다면 400 코드 전달하고 클라이언트 오류를 출력함으로써 유효하지 않은 요청을 했음을 알림
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def fbv_detail(request, pk):
    try:
        # 요청 데이터가 있다면 변수에 담고
        fbv_post = fbv_Post.objects.get(pk=pk)
        # 데이터가 없으면 404 에러 출력
    except fbv_Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # 만약 상세 페이지 보여달라고 GET 요청이 들어온거면
    if request.method == 'GET':
        # pk값이 지정된 쿼리셋을 fbv_PostSerializer를 통해 인스턴스화 하고
        serializer = fbv_PostSerializer(fbv_post)
        # 인스턴스의 데이터를 보여줘
        return Response(serializer.data)
    # 수정 요청이 들어온다면
    elif request.method == 'PUT':
        # 원래 저장된 데이터도 인스턴스화하고 수정요청한 데이터도 인스턴스화 해줘
        # 왜냐면 사용자가 수정버튼을 눌렀을 때 저장되어있던 데이터를 보여줘야 어디서 수정할지를 판단하고
        # 판단한 내용으로 수정한 데이터를 다시 request.data로 보낼테니까
        serializer = fbv_PostSerializer(fbv_post, request.data)

        # 그럼 request.data에 대해서도 검증을 해야지
        if serializer.is_valid():
            # 유효한 데이터면 저장을 하고
            serializer.save()
            # 사용자가 최종 수정한 데이터를 응답해주면 됨
            return Response(serializer.data)
        # 유효한 데이터가 아니면 에러 출력해주면 되고
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 삭제 요청을 한다면
    elif request.method == 'DELETE':
        # pk값이 지정된 쿼리셋을 지워라!
        fbv_post.delete()
        # 그리고 본문이 없다고 응답 코드를 주면 됨
        return Response(status=status.HTTP_204_NO_CONTENT)
```



```python
# urls.py
from django.urls import path
from . import views

app_name = 'fbvapp'

urlpatterns = [
    path('fbv_post/', views.fbv_post_list),
    path('fbv_post/<int:pk>/', views.fbv_detail),
]
```



> 회원가입, 로그인, 로그아웃 - 사용자 관련

![이미지](https://media.discordapp.net/attachments/1045319564340252681/1047338010447990794/unknown.png)

- DRF를 적용하기 전에는 django.contrib.auth를 통해 AbstractUser를 가져오고 form에서 UserCreationForm, UserChangeForm을 활용하고, 이 form 안에 들어가는 데이터를 get_user_model()로 가져왔었음.

- DRF를 이용해서 로그인, 로그아웃을 하려면 django-allauth를 활용하고, 회원가입을 직접 만드는 것이 아니라 만들어진 패키지를 활용하려면 django-rest-auth를 활용하면 된다고 하는데.. 근데 검색해보면 JWT라는 개념이 많이 나옴. JSON Web Token Authentication이라고 하는데, DRF가 JSON을 다루기 위해 나온 형태라고 본다면 JSON을 쓰는 것도 이해가 되는데, 왜 인증방식은 Token을 채택하는가?

  - https://velog.io/@junghyeonsu/%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%90%EC%84%9C-%EB%A1%9C%EA%B7%B8%EC%9D%B8%EC%9D%84-%EC%B2%98%EB%A6%AC%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95
  - HTTP 비연결성 때문에 서버-클라이언트 간에는 주기적으로 통신해서 인증된 사용자임을 검증받아야 함.
  - 이 검증 방식 중 session은 보안성이 높으나 서버에서 사용자의 세션 정보를 저장하기 때문에 사용자가 많아지면 많아질 수록 session 검증을 위한 자원이 많이 필요하게 됨.
  - token은 서버로부터 발급받은 token을 사용자 브라우저에 저장하고 필요할 때 이 토큰 값만 넘겨줌으로써 서버에서 유효한 token인지를 검증하기 때문에 서버에서 인증을 위해 많은 리소스를 투입하지 않아도됨. (물론 사용자의 부주의로 해킹당해 token값을 탈취당하는 등 보안성 리스크는 세션보다는 큼)

  



> 회원가입, 로그인 구현

- JWT + DRF(FBV) 이용
- 참고 블로그: https://toload.tistory.com/entry/Django-DRF-%EC%BB%A4%EC%8A%A4%ED%85%80-%EC%9C%A0%EC%A0%80-%EB%AA%A8%EB%8D%B8-%EC%83%9D%EC%84%B1-%EB%B0%8F-%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85-%EB%A1%9C%EA%B7%B8%EC%9D%B8-JWT-%EC%A0%81%EC%9A%A9
- 일단 DRF를 통해 1) 사용자의 MBTI 정보를 담는 커스텀 DB가 필요했고, 2) Django 학습을 Function base로 진행했기 때문에 FBV로 구현해야 했으며, 3) 가장 많이 쓰는 JWT 모듈을 통해 DRF 모델을 만드는 것이 목표.
- 하지만 하기 코드들을 테스트 했을때 2022.12.01 현재 accounts/views.py의 login 함수에서 authenticate 함수가 제대로 동작하지 않고 username, password를 넣었을 때 등록된 사용자임에도 불구하고 None을 출력하는 이슈가 있음. 이는 향후 해결해야하는 부분으로 인지.

```python
# 패키지 설치
$ pip list
Package                       Version
----------------------------- ---------
...
Django                        3.2.13
django-rest-authtoken         2.1.4
djangorestframework           3.14.0
djangorestframework-simplejwt 5.2.2
...
```



```python
# pjt/settings.py
...
INSTALLED_APPS = [
    # 계정 관련 생성한 App
    'accounts',
	
    ...
	
    # JWT 적용을 위한 패키지
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
]
...
# User 모델 커스텀을 위한 AUTH_USER_MODEL 상속
AUTH_USER_MODEL = 'accounts.User'

## DRF 
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  # 인증된 요청인지 확인
        'rest_framework.permissions.IsAdminUser',  # 관리자만 접근 가능
        'rest_framework.permissions.AllowAny',  # 누구나 접근 가능
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # JWT를 통한 인증방식 사용
    ),
}

REST_USE_JWT = True

## JWT
# 추가적인 JWT_AUTH 설젇
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}
```



```python
# pjt/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('accounts.urls')),
]
```



```python
# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):   
    nickname = models.CharField(max_length=30)    
    mbti1 = models.CharField(null=True, max_length=1)
    mbti2 = models.CharField(null=True, max_length=1)
    mbti3 = models.CharField(null=True, max_length=1)
    mbti4 = models.CharField(null=True, max_length=1)
    gender = models.CharField(null=True, max_length=1)
    age = models.IntegerField(null=True)
```



```python
from .models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

# 패스워드가 필요없는 다른 테이블에서 사용할 용도
class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
```



```python
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login

from accounts.serializers import UserSerializer



@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    username = request.data.get('username')
    password = request.data.get('password')
    nickname = request.data.get('nickname')

    serializer = UserSerializer(data=request.data)
    serializer.username = username
    serializer.nickname = nickname

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(password)
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    print(username, password)
    user = authenticate(username=username, password=password)

    print(user)
    if user is None:
        return Response({'message': '아이디 또는 비밀번호가 일치하지 않습니다.'}, status=status.HTTP_401_UNAUTHORIZED)

    refresh = RefreshToken.for_user(user)
    update_last_login(None, user)

    return Response({'refresh_token': str(refresh),
                     'access_token': str(refresh.access_token), }, status=status.HTTP_200_OK)
```



```python
from django.urls import path, include
from . import views


app_name = 'accounts'

login_patterns = [
    path('normal/', views.login, name='login'),
]

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', include(login_patterns)),
]
```





> DRF의 인증, 권한을 잘 설명해둔 블로그.

https://velog.io/@duo22088/DRF-Authentication-%EA%B3%BC-Permissons