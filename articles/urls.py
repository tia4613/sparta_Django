from django.urls import path
from . import views #.은 내 위치

app_name = 'articles'
urlpatterns = [

    path('', views.articles, name='articles'),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/comments/", views.comment_create, name="comment_create"),

    path('data_throw/', views.data_throw, name='throw'),
    path('data_catch/', views.data_catch, name='catch'),
]