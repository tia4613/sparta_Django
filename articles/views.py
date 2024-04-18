from django.shortcuts import render, redirect
from .models import Article


def index(request):
  return render(request, "index.html")

def articles(request):
  articles = Article.objects.all().order_by("-created_at")
  context = {
        "articles": articles,
    }
  return render(request, "articles.html", context)

def detail(request, pk):
  article = Article.objects.get(pk=pk)
  context = {
    "article": article,
    }
  return render(request, "detail.html", context)

def new(request):
    return render(request, "new.html")

def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")

    article = Article(title=title, content=content)
    article.save()
    return redirect("detail", article.id)

def delete(request, pk):
  article = Article.objects.get(pk=pk)
  if request.method == "POST":
      article.delete()
      return redirect("articles")
  return redirect("detail", article.pk)

def data_throw(request):
  return render(request, "data_throw.html")

def data_catch(request):
  message = request.GET.get("message")
  context = {
      "message" : message,
		}
  return render(request, "data_catch.html", context)

