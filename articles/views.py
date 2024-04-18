from django.shortcuts import render
from .models import Article


def index(request):
  return render(request, "index.html")

def articles(request):
  articles = Article.objects.all()
  context = {
        "articles": articles,
    }
  return render(request, "articles.html", context)

def data_throw(request):
  return render(request, "data_throw.html")

def data_catch(request):
  message = request.GET.get("message")
  context = {
      "message" : message,
		}
  return render(request, "data_catch.html", context)

