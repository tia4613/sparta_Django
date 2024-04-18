from django.shortcuts import render


def index(request):
  return render(request, "index.html")

def articles(request):
  return render(request, "articles.html")

def data_throw(request):
  return render(request, "data_throw.html")

def data_catch(request):
  message = request.GET.get("message")
  context = {
      "message" : message,
		}
  return render(request, "data_catch.html", context)

