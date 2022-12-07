from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns =[
    path('', views.BlogList.as_view()),
    path('<int:pk>/', views.BlogDetail.as_view()),
    path('<int:pk>/comments', views.Commentlist.as_view()),
    path('<int:blog_pk>/comments/<int:comment_pk>', views.Commentdetail.as_view()),
    path('<int:pk>/like', views.Likelist.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)