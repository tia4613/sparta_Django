"""
URL configuration for my_first_pjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from articles import views

# urlpatterns는 어떤 path로 들어왔을 때 어디로 보낼지
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),   
    path('hello/', views.hello),
    path('data_throw/', views.data_throw),
    path('data_catch/', views.data_catch),

    path('users/', views.users),
    path("users/<str:username>/", views.profile),

]
