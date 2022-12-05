## Authentication / Permission / Throttiling 구분

1.  **Authentication(인증)** : 유저 식별

2. **Permission(허가)** : 유저 식별 후, 해당 유저의 요청에 대한 허용/거부 결정

3.  **Throttling** : 허용된 유저에 대해, 일정 기간 동안에 허용할 최대 요청 횟수



### 인증(Authentication) 처리 순서

1. 매 요청 시마다 APIView의 dispatch(requet) 호출

2. APIView의 initial(request) 호출
3. APIView의 perform_authentication(request) 호출

4. request의 user속성 호출( rest_framework.request.Request 타입 )

5. request의 _authenticate() 호출 → 실제 인증 여부 체크, 인증에 실패하면 not_authenticated() 멤버함수



### 지원하는 인증 (Authentication) 종류

**SessionAuthentication**

- 일반 웹에서 사용
- 한번만 로그인하면 정보가 세션에 저장되어 있음
- APIView에서 디폴트 지정

**BasicAuthentication**

- 매 요청마다 요청 헤더에다 Basic 인증 정보를 담아 인증 (ex. Authorization: Basic YWxsaWV1cxE6MTAoXYWtl)   → Basic 뒤에 부분은 유저명:암호라 요청을 보낼때 보안을 위해 반드시 https 프로토콜 사용해야함 
- HTTPie를 통한 요청 : http --auth 유저명:암호 --form POST :8000 필드명1:값1 필드명2:값2

**TokenAuthentication**

- 매 요청마다 요청 헤더에다 Token 정보를 담아 인증 ( ex. Authorization: Token 401f54qkadfijaojkgjaljfdjdflkjfe)
- 랜덤을 통해서 각 유저마다 유니크한 토큰을 할당받으며, 토큰만 있으면 인증됨
- 토큰에 대한 유효성 만료가 없고 유저별로 하나만 할당되기에 유출되면 위험하므로 요즘에는 JWT를 주로 사용



### *DRF의 허가(Permission)* 

현재 요청에 대한 허용/거부를 결정하며 APIView 단위로 지정 가능하다

 

#### DRF의 permission

- **AllowAny** ( 디폴트 전역 설정 ) : 인증 여부에 상관없이, 뷰 호출 허용
- **IsAuthenticated** : 인증된 요청에 한해서, 뷰 호출 허용
- **IsAdminUser** : staff인증 요청에 한해서, 뷰 호출 허용
- **IsAuthenticatedOrReadOnly** : 비인증 요청에게는 읽기/조회만 허용

 