from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("blog/", views.BlogList.as_view()),
    path("blog/<int:pk>/", views.BlogDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
