## django => web framework

> 브라우저에 대응되는 js, html, css는 한계 => 안드로이드나 ios는 사용을 안 하기 때문

> 멀티플랫폼에 대응하기 위한 필요성을 위해 django rest framework 사용



#### DRF를 사용하는 이유

- 웹 브라우저 API는 범용성이 크고 개발을 쉽게 만들어 줍니다.
- ORM & non-ORM에 대해 모두 Serialization 기능을 제공해줍니다. (DB data -> Json)
- 문서화와 커뮤니티 지원이 잘 되어 있습니다.
- 프론트엔드와 백엔드 분리가 가능



### Rest : 

1. http 프로토콜 사용

2. 자원관리가 편리

3. 플랫폼이 독립적(다른 것에 종속X)



Representational State Transfer



### mvc

> model view controller대신 template 대신 model과 view에 집중

- model => 데이터베이스 관리 (row => columns // article => title, article, image)



#### model

- ORM(object relational mapping, 객체-관계-매핑 ) 기술 활용 sql 사용 없이 db 연결

- 객체와 데이터베이스의 관계를 매핑해주는 도구
- 프로그래밍 언어의 객체와 관계형 데이터베이스의 데이터를 자동으로 매핑(연결)해주는 도구
- **MVC 패턴에서 모델(Model)을 기술하는 도구**
- **객체와 모델 사이의 관계를 기술하는 도구**



### ORM 사용 이유

> 직관적인 코드(가독성) + 비지니스 로직 집중 가능 (생산성)



#### view

- request(요청) // response(응답)
- 유저가 보는 화면을 보여주게 하는 역할



#### 라우팅(routing)

- user -(request)->  server   => urls.py 에서 연결
- **네트워크와 네트워크 간의 경로(Route)를 설정하고 가장 빠른 길로 트래픽을 이끌어주는 네트워크 장비**



```python
# SimpleRouter

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'accounts', AccountViewSet)
urlpatterns = router.urls
```





참고 : [django rest framework 공식문서](https://www.django-rest-framework.org/)



`vue 서버 열기`   -> `npm run serve`

