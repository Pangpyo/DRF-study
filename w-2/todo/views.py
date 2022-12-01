from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .serializers import TODOserializers
from .models import TODO
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Create your views here.

# django REST Framework - authentication

# 1. BasicAuthentication: HTTP 제어 header로 넘긴 id와 password를 base64로 encoding (보안 상의 위협이 있을 수 있음, 테스트에 적절)

# 2. TokenAuthentication: 해당 방식은 token으로 인증, 인증 요청을 보낼 시 key 값을 되돌려주는 방식 (client-server 관계에서 사용하기에 적절)

# 3. SessionAuthentication: 로그인될 때마다 저장되는 session 정보를 통해 인증

# 4. RemoteAuthentication: user 정보가 다른 서비스에서 관리될 때 쓰이는 방식

# 5. Custom Authentication: 개발자가 custom 하게 authentication을 만들어서 사용할 수도 있음


# Django REST Framework - permission

# 1. AllowAny: 인증/비인증 모두 허용 (default)

# 2. IsAuthenticated: 인증된 요청에 대해서만 view 호출

# 3. IsAdminUser: Staff User에 대해서만 요청 허용 (User.is_staff가 True여야 함)

# 4. IsAuthenticatedOrReadOnly: 비인증 요청에 대해서는 읽기만 허용

# 5. DjangoModelPermissions: 사용자 인증과 관련 모델 권한이 할당된 경우 허용 (django.contrib.auth 모델 permission과 관련 있음)

# 6. DjangoModelPermissionOrAnonReadonly: DjangoModelPermission과 유사, 비인증 요청에 대해서는 읽기만 허용

# 7. DjangoObjectPermissions: 모델에 대한 객체 별로 권한이 할당된 경우 허용

# 8. Custom Permission: 개발자가 custom 하게 permission을 만들어서 사용할 수도 있음


class TODOViewSet(viewsets.ModelViewSet):
    # authentication_classes = [BasicAuthentication, SessionAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = TODO.objects.all()
    serializer_class = TODOserializers
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ["title", "user", "is_complete"]
    search_fields = "title"
    ordering_fields = ("is_complete", "created_at", "updated_at")
