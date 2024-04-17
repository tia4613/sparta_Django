from django.shortcuts import render


def index(request):
	return render(request, "index.html")

def users(request):
	return render(request, "users.html")

def hello(request):
	# 변수 선언 - 이름을 바꿔준다
	context = { 
		"name":"hwan",
	}
	return render(request, "hello.html",context)