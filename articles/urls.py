from django.urls import path
from . import views #.은 내 위치

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('data_throw/', views.data_throw, name='data_throw'),
    path('data_catch/', views.data_catch, name='data_catch'),
]