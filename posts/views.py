from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

def index(request):
	#return HttpResponse('Hello') 
	posts=Posts.objects.all()[:10]

	context={
		'title':'Latest Posts',
		'posts':posts
	}
	return render(request, 'posts/index.html',context)

def details(request,id):
	posts=Posts.objects.get(id=id)

	context={
		'posts':posts
	}
	return render(request,'posts/details.html',context)