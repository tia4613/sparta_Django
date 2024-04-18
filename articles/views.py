from django.shortcuts import render


def index(request):
  return render(request, "index.html")

def users(request):
  return render(request, "users.html")

def hello(request):
  name = 'hwan'
  tags = ["python","css","html"]
  books = ['어린왕자', '백설공주','신데렐라']

  context = { 
    "name": name,
    "tags": tags,
    "books": books,
  }
  return render(request, "hello.html",context)

def data_throw(request):
  return render(request, "data_throw.html")

def data_catch(request):
  message = request.GET.get("message")
  context = {
      "message" : message,
		}
  return render(request, "data_catch.html", context)