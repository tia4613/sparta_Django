from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods


def index(request):
  return render(request, "articles/index.html")

def articles(request):
  articles = Article.objects.all().order_by("-created_at")
  context = { "articles": articles,}
  return render(request, "articles/articles.html", context)

def detail(request, pk):
  article = get_object_or_404(Article, pk=pk)
  comment_form = CommentForm()
  comments = article.comments.all().order_by("-pk")
  context = { 
    "article": article,
    "comment_form" : comment_form,
    "comments" : comments
  }
  return render(request, "articles/detail.html", context)

@login_required
def create(request):
  if request.method == "POST":
      form = ArticleForm(request.POST, request.FILES)
      if form.is_valid():
          article = form.save()
          return redirect("articles:detail", article.id)
  else:
      form = ArticleForm()

  context = {"form": form,}
  return render(request, "articles/create.html", context)

def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("articles:detail", article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        "form": form,
        "article": article,
    }
    return render(request, "articles/update.html", context)

@require_POST
def delete(request, pk):
  if request.user.is_authenticated:
    article = get_object_or_404(Article, pk=pk)
    article.delete()
  return redirect("articles:articles")

@require_POST
def comment_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect("articles:detail", article.pk)


@require_POST
def comment_delete(request, pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect("articles:detail", pk)





def data_throw(request):
  return render(request, "articles/data_throw.html")

def data_catch(request):
  message = request.GET.get("message")
  context = {
      "message" : message,
		}
  return render(request, "articles/data_catch.html", context)

