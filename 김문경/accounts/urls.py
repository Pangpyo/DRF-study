from accounts.views import hello_world, hello_world_drf
from django.urls import path

urlpatterns = [
    path('hello_world/', hello_world),
    path('hello_world_drf/', hello_world_drf),
]


