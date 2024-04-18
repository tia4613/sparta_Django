from django.shortcuts import render
from .models import Article


def index(request):
  return render(request, "index.html")

def articles(request):
  articles = Article.objects.all().order_by("-created_at")
  context = {
        "articles": articles,
    }
  return render(request, "articles.html", context)

def new(request):
    return render(request, "new.html")

def create(request):
    # GET 방식으로 전달된 데이터를 받아서
    title = request.GET.get("title")
    content = request.GET.get("content")

    # 받은 데이터를 Article 모델을 이용해서 저장
    article = Article(title=title, content=content)
    article.save()
    context = {
        "article": article,
    }
    return render(request, "create.html", context)

def data_throw(request):
  return render(request, "data_throw.html")

def data_catch(request):
  message = request.GET.get("message")
  context = {
      "message" : message,
		}
  return render(request, "data_catch.html", context)

