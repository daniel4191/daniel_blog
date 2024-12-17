from django.urls import path
from . import views


urlpatterns = [
    # FBV 방식의 패턴
    # path('', views.index),
    # path('<int:pk>/', views.single_post_page)

    # CBV 방식의 패턴
    path("", views.PostList.as_view()),
    path("<int:pk>/", views.PostDetail.as_view())

]