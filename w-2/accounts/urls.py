from django.contrib import admin
from django.urls import path, include
from .views

urlpatterns = [
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    # 구글 소셜로그인
    path("google/login", google_login, name="google_login"),
    path("google/callback/", google_callback, name="google_callback"),
    path("google/login/finish/", GoogleLogin.as_view(), name="google_login_todjango"),
]
