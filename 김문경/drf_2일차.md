# 🗓️11월 29일 2회차

# 과제 : 유저 - 게시글 + 인증/권한 DRF로 만들어 보기

> 참고자료 : https://velog.io/@lemontech119/DRF%EB%A1%9C-%EC%84%9C%EB%B2%84-%EA%B0%9C%EB%B0%9C1-%ED%9A%8C%EC%9B%90%EA%B8%B0%EB%8A%A5

## 🧩유저

### ✔️라이브러리 활용

**djangorestframework**: Django를 REST API 형태로 사용할 수 있도록 도와줍니다.

**dj-rest-auth**: REST API 형태로 제공해주는 로그인, 비밀번호 찾기 등의 기능을 제공합니다. (django-rest-auth라는 라이브러리가 더 이상 개발되지 않음에 따라 생긴 프로젝트)

**django-allauth**: 회원가입 기능을 제공합니다.

**djangorestframework-simplejwt**: Django에서 JWT Token을 사용하도록 도와줍니다.

<br>

### 🧩게시글

일단 create, read 까지 구현

