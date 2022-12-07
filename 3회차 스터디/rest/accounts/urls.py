from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('', include('dj_rest_auth.urls')),
]