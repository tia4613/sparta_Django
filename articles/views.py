from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


def index(request):
  return render(request, "index.html")

def articles(request):
  articles = Article.objects.all().order_by("-created_at")
  context = { "articles": articles,}
  return render(request, "articles.html", context)

def detail(request, pk):
  article = Article.objects.get(pk=pk)
  context = { "article": article,}
  return render(request, "detail.html", context)

def create(request):
  if request.method == "POST":
      form = ArticleForm(request.POST)
      if form.is_valid():
          article = form.save()
          return redirect("detail", article.id)
  else:
      form = ArticleForm()

  context = {"form": form,}
  return render(request, "create.html", context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("article_detail", article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        "form": form,
        "article": article,
    }
    return render(request, "update.html", context)

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

